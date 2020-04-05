from datetime import datetime
from flask_login import UserMixin, current_user
from core import db, login_manager
from .utils import encrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(UserMixin, db.Model):
    """
    Classe para representação do usuário no banco de dados.

    Parâmetros:
        username: nome de usuário.
        email: email do usuário.
        password: senha so usuário.
        name (opcional): nome completo do usuário.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=True)

    def __init__(self, username, email, password, name=None):
        self.name = name
        self.username = username
        self.email = email
        self.password = encrypt(password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return f'{self.id}'

    @property
    def has_followed(self):
        return Follow.query.filter_by(user_id=self.id).filter_by(follower_id=current_user.id).first() is not None

    def user_followers_id(self):
        users = []
        user_followers = Follow.query.filter_by(follower_id=current_user.id).all()
        for user in user_followers:
            users.append(user.user_id)

        users.append(current_user.id)
        return users

    def __repr__(self):
        return f'<User: {self.username}>'


class Tweet(db.Model):
    """
    Classe para representação de um tweet no banco de dados.

    Parâmetros:
        content: conteúdo do tweet.
        user_id: id do usuário que publicou o tweet.
    """
    __tablename__ = "tweet"

    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'<Tweet: {self.id}>'


class Follow(db.Model):
    """
    Classe para representação de um seguidor no banco de dados.
    """
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id

    @property
    def has_followed(self):
        return Follow.query.filter_by(user_id=self.user_id).filter_by(follower_id=current_user.id).first() is not None
