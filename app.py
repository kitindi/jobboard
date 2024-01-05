from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


"""
Auto reloading flask app
$ --> flask --app app.py --debug run
"""