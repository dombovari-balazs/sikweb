import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
import data_manager

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

allowed_email = ["asd@asd.hu"]
allowed_password = ["123"]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/inner/<email>')
def inner(email):
    return render_template("index_innerpage.html", email=email)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('upload.html')


@app.route('/gallery')
def gallery():
    files = data_manager.get_file_names()
    print(files)
    return render_template('gallery.html', files=files)


@app.route('/news')
def news():
    return render_template("news.html")


@app.route('/profile/<email>')
def profile(email):
    return render_template('profile.html', email=email)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    email = request.form.get('email')
    password = request.form.get('password')
    global allowed_email
    global allowed_password

    if email in allowed_email and password in allowed_password:
        return redirect('/inner/' + email)


if __name__ == '__main__':
    app.run()
