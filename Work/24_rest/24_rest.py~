#Bob - Jerry Ye and JiaJie Mai
#SoftDev1 pd7
#K24 - A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template, request
import urllib, json

app = Flask(__name__)

@app.route('/')
def index():
    output = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=XZ5YhAvHZNp90JaM7AUZORCL27mkB8V8x7U2YEny')
    string = output.read()
    dictonary = json.loads(string)
    return render_template('24_rest.html',picture=dictonary['url'],caption=dictonary['explanation'],date=dictonary['date'])


if (__name__) == "__main__":
    app.debug = True
    app.run()
