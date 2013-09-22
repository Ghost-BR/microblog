from flask import flash, redirect, render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Christofer'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!',
        },
    ]
    return render_template('index.html',
        title='Home',
        user=user,
        posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        msg = 'Login requested for OpenID="%s", remember_me=%s'
        flash(msg % (form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title='Sign In',
        form=form,
        providers=app.config['OPENID_PROVIDERS'])
