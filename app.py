from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def start():
    return 'Server is Running'

@app.route('/hdps')
def home():
    return render_template("index.html")