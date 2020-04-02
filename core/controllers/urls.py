from flask import render_template
from flask import request
from core import app, db
from core.models.forms import LoginForm, UserCreationForm
from core.models.tables import User


@app.route('/')
@app.route('/login/')
def index():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/cadastro/', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()

    if request.method == 'POST' and form.validate_on_submit():
        user_by_username = User.query.filter_by(username=form.username.data).all()
        user_by_email = User.query.filter_by(email=form.email.data).all()

        if user_by_email or user_by_username:
            message = "Nome de usuário ou email já cadastrados."
            class_name = "has-text-danger"
        else:
            user = User(
                form.username.data, 
                form.email.data,
                form.password.data,
                form.name.data
                )
            db.session.add(user)
            db.session.commit()
            message = "Usuário cadastrado com sucesso."
            class_name = "has-text-success"

        return render_template(
            'signup.html',
            form=form,
            message=message,
            class_name=class_name
        )

    return render_template('signup.html', form=form)


@app.route('/home/')
def home():
    return render_template('home.html')
