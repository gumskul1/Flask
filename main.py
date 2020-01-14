from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return "<h1><a href='/about'>My home<a/></h1>"

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/contact')
def contact():
  return render_template('contact.html',Phone=12345678)



app.run(host = '0.0.0.0', port = 8020)
#ieej heroku