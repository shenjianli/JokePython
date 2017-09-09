from flask import Flask
import JokeDB
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Shen!'

# http://127.0.0.1:5000/index/   #访问这个会报错的
@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/joke_json/test')
def query_joke_json():
    joke = JokeDB.query_mysql_data()
    joke_json = json.dumps(joke, ensure_ascii=False)
    print(joke_json)
    return  joke_json


if __name__ == '__main__':
    app.run()