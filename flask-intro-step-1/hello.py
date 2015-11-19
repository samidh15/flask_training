from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def show_url_for():
    return url_for('show_user_profile',
                   username='foo')
@app.route('/user/<username>')
def show_user_profile(username):
    return 'user: %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post: %d'%post_id


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    i = 1
    return 'Hello Loser'

if __name__ == '__main__':
    app.debug = True
    app.run()
