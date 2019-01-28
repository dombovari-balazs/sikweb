from flask import Flask, render_template, request

app = Flask(__name__)


allowed_email = ["asd@asd.hu"]
allowed_password = ["123"]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form.get('email')
    password = request.form.get('password')
    global allowed_email
    global allowed_password

    if email in allowed_email and password in allowed_password:
        return render_template("index_innerpage.html")


if __name__ == '__main__':
    app.run()