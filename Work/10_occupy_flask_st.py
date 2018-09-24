#Jiajie Mai
#softDev Pd 07
#hw 10: Jinja Tuning

#Help from Liang for occupation code
#Gave up after some time, couldn't understand how to fix the problem as I have no knowledge in Python to work this out

#imports random and csv
import random, csv
from flask import Flask, render_template

app = Flask (__name__)

#setting up the resources
source = open('occupations.csv', 'rU')
reader = csv.reader(source)

dict = {}
for line in reader:
	dict[line[0]] = line[1]

def getKey(dict):
	copy = {}
	for key in dict:
		copy[key] = dict[key]
	copy.pop('Total')
	result = random.random() * 100
	sum = 0
	for key in copy:
		sum += float(copy[key])
		if sum >= result:
			return key

@app.route("/")               
def hello():
    return "Go to occupations for the work"

@app.route("/occupations")
def jobs():
    return render_template("foo.html", job = getKey(dict), chart = disc)



app.run(debug=True)

