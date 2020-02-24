from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect , request
import os
from model.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

# fonction main
app = Flask(__name__)

app.config.update(

    SECRET_KEY='5791628bb0b13ce0c676dfde280ba245',
    SQLALCHEMY_DATABASE_URL='PostgeSQL 10://postgres/5630/localhost/exemple',
    SQLALCHEMY_TRACK_MODIFICATIONS= 'false'
)

db=SQLAlchemy(app)

@app.route("/about")
def about():
    return render_template('about_admin.html', title='About')


# les ddifférentes fonctions et macros de notre application

posts = [
    {
        'author': 'Brice SOME',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': ''
    },
    {
        "author": "Jean Olivier",
        "title": "Blog Post 2",
        "content": "First post content",
        "date_posted": ''
    }
]



# Les différentes routes de notre application

        # classe publication
class Publication(db.Model):
    __tablename__='publication'

    id = db.Column(db.Integer,primary_key=True)
    nom =db.Column(db.String(30),nullable=False)

    def __init__(self,nom):
        self.nom=nom

    def __repr__(self):
        return 'le id est : {} , et  le nom est : {}'.format(self.id,self.nom)


@app.route("/home")
def home():
    return render_template('home_admin.html', posts=posts)


@app.context_processor
def inject_now():
    return {'now': datetime.now().strftime(("%Y-%m-%d  %H:%M:%S"))}





@app.route("/tkinter")
def tkinter():
    return render_template('test.py', title='page tkinter ici !!!!!')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('home_admin.html', title='Register', form=form)

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login_user.html', title='Login user', form=form ,now=datetime.utcnow())


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login_admin.html', title='Login admin', form=form ,now=datetime.utcnow())

# les routes de retour vers les pages html bien specifique comme : page html de l'admin , ...
@app.route("/admin_home")
def admin_home():
    return render_template('home_admin.html', title='About')

@app.route("/user_home")
def user_home():
    return render_template('home_user.html', title='About')


