import os
import psycopg2
from config import config


def get_picture_names():
    return os.listdir('static/images')


def connect(command):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read the connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        cur.execute(command)
        table = cur.fetchall()

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQl
        cur.close()
        return table
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def print_table_from_SQL():
    command = ("""
     SELECT * FROM persons 
     """)
    table = connect(command)
    print("The table is: ", table)

if __name__ == '__main__':
    print_table_from_SQL()
