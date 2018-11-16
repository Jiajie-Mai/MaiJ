#Jiajie Mai
#SoftDev1 pd7
#K25-Getting More REST
#2018-11-14

from flask import Flask, render_template, request

import urllib, json

app = Flask(__name__)


@app.route('/')
def index():
    output = urllib.request.urlopen('mtaapi.herokuapp.com/stop?id=120')
    string = output.read()
    dictonary = json.loads(string)
    return render_template('25_rest.html', lat = dictonary['result']['lat'], lon = dictonary['result']['long'], name = dictonary['result']['name'])
    
if (__name__) == "__main__":
    app.debug = True
    app.run()
