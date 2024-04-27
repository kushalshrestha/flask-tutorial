from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/home')
def home():
    css_url = url_for('static', filename='style.css')
    return f'<link rel="stylesheet" type="text/css" href="{css_url}">' + '<p>Index Page</p>'

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/<name>')
def hello(name):
    return f"<p>Hello, {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"You are viewing post id: {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'The subpath is: {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST method called'
    else:
        return 'GET method called'
    
@app.get('/login')
def login_get():
    return 'GET method called'

@app.post('/login')
def login_post():
    return 'POST method called'


with app.test_request_context():
    print(url_for('index')) # Generates "/"
    print(url_for('hello_world'))   # Generates "/hello"
    print(url_for('hello', name='Kushal Shrestha')) # Generates "/hello/Kushal%20Shrestha"
    print(url_for('show_post', post_id=1))    # Generates "/post/1"
    print(url_for('show_subpath', subpath='a/b/c'))  # Generates "/path/a/b/c"
     
    