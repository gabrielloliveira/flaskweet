from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required, login_user, current_user, logout_user
from core import app, db, login_manager
from core.models.forms import LoginForm, UserCreationForm
from core.models.tables import User, Tweet
from core.models.auth import authenticate


@app.route('/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = authenticate(form.username.data, form.password.data)
        if user:
            login_user(user)
            return redirect(url_for('home'))

        message = "Email ou senha inválidos."
        class_name = "has-text-danger"
        return render_template(
            'login.html',
            form=form,
            message=message,
            class_name=class_name
        )

    return render_template('login.html', form=form)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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


@app.route('/logout/', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home/')
@login_required
def home():
    tweets = Tweet.query.filter_by(user_id=current_user.id).order_by(Tweet.pub_date.desc()).all()
    return render_template('home.html', tweets=tweets)


@app.route('/publish/', methods=['POST'])
@login_required
def publish_tweet():
    content = request.form['content']
    tweet = Tweet(content, current_user.id)
    db.session.add(tweet)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/search/user/', methods=['GET'])
@login_required
def search_user():
    username = request.args['username']
    users = User.query.filter(User.username.contains(username)).all()
    return render_template('search.html', users=users)
