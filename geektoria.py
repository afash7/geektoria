from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)