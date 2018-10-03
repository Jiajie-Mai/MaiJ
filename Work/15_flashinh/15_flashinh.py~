#Jiajie Mai
#SoftDev1 pd7
#K14 Do I Know You?
#2018-10-01

import os
from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = os.urandom(32)

username = 'Jiajie'
password = 'Mai'


@app.route('/')
def login():
    if ('username' in session):
        return render_template('welcome.html', username_input = session['username'])
    else:
        return render_template('input.html')

@app.route('/auth')
def authenticate():
    if (request.args['username'] != username or request.args['password'] != password):
        return render_template('incorrect.html')
    
    else:
        session['username'] = username
        return render_template('welcome.html', username_input = request.args['username'])

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')



app.debug = True
app.run()



