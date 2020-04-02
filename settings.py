import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "flaskweet/storage.db")

SECRET_KEY = "ltoy9v6omr+1jd-st(c@oj#d^ofqfr0j3sqrsnr+4p10d7%imi"
ENV = "development"
DEBUG = True
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_DIR}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
