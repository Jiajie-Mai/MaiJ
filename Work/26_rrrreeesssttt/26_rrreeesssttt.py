#Jiajie Mai
#SoftDev1 pd7
#K24 - rrreeesssttt
#2018-11-15
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
    
    apikey = 'ae76c0ee10a51afb0360ca59edc8eee7605a35f0'
    url='https://www.calendarindex.com/api/v1/holidays?country=US&year=2018&state=NY&api_key='
    output = urllib.request.urlopen(url+apikey)
    string = output.read()
    dictonary = json.loads(string)
    second_one = dictonary['response']['holidays']
    
    url = 'https://api.adviceslip.com/advice'
    utput = urllib.request.urlopen(url+apikey)
    string = output.read()
    dictonary = json.loads(string)
    third_one = dictonary['slip']['advice']
    
    return render_template('rrreeesssttt.html',one=first_one,two=second_one,three=third_one)

if (__name__) == "__main__":
    app.debug = True
    app.run()
