from passlib.hash import pbkdf2_sha256


def encrypt(password):
    return pbkdf2_sha256.hash(password)


def verify(password, password_storaged):
    return pbkdf2_sha256.verify(password, password_storaged)
