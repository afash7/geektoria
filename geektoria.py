from flask import Flask, render_template
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bf0e8df64ec4fa5fd85cdbe35a7fa5a4'

posts = [
    {
        'author': 'Afash',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'apr 22, 2024'
    },
    {
        'author': 'jane doe',
        'title': 'blog post 2',
        'content': 'secend post content',
        'date_posted': 'apr 28, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)