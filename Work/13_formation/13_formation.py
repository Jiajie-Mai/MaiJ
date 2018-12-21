from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def choice():
    return render_template('input.html')


@app.route("/auth", methods = ["GET"])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.headers)
    return render_template('greet.html', username = request.args["Username"], request_type = request.method )

app.debug = True
app.run()
