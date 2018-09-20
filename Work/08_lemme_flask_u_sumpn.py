from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return 'Welcome to the Homepage. <a href="/hello">Hello Page</a> <a href="/otherpage">Other page.</a>'


@app.route("/hello")
def hello():
    return 'This is the Hello Page. <a href="/">Home</a>'


@app.route("/otherpage")
def otherpage():
    return 'This is another page. <a href="/">Home</a>'


app.run(debug=True)
