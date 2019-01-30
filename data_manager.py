import connection

def get_file_names():
    return connection.get_picture_names()


def password_validator(password):
    allowed_password = ["123"]

    if password in allowed_password:
        return True
    else:
        return False


def email_validator(email):
    allowed_email = ["asd@asd.hu"]
    if email in allowed_email:
        return True
    else:
        return False


