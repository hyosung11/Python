from flask import Flask
app = Flask(__name__)
print(__name__)

# decorator
@app.route('/')
def hello_world():
    return 'I love SungOh and Omi'


@app.route('/blog')
def blog():
    return 'Welcome to my blog'


@app.route('/blog/2020/dogs')
def blog2():
    return 'This is the dog I want.'
