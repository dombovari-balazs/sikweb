def get_file_names():
    names = ['images/3944415-bing-wallpapers.jpg', 'images/dd1_.jpg','images/TrollFace.jpg', 'images/x-3.png']
    return names


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


