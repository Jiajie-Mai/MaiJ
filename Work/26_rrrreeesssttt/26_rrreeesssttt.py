#Jiajie Mai
#SoftDev1 pd7
#K24 - rrreeesssttt
#2018-11-15

#I'm not gonna lie but this took way too long and I just gave up
from flask import Flask, render_template, request
import urllib, json

app = Flask(__name__)

@app.route('/')
def first():
    url = 'http://api.icndb.com/jokes/random'
    output = urllib.request.urlopen(url)
    string = output.read()
    dictonary = json.loads(string)
    first_one = dictonary['value']['joke']
    
    url='https://www.boredapi.com/api/activity'
    output = urllib.request.urlopen(url)
    string = output.read()
    dictonary = json.loads(string)
    second_one = dictonary['activity']
    
    url = 'https://api.adviceslip.com/advice'
    utput = urllib.request.urlopen(url)
    string = output.read()
    dictonary = json.loads(string)
    third_one = dictonary['slip']['advice']
    
    return render_template('rrreeesssttt.html',one=first_one,two=second_one,three=third_one)

if (__name__) == "__main__":
    app.debug = True
    app.run()
