from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template("home.html", aktiva_lapa = 'home')

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/contact')
def contact():
  return render_template('contact.html',phone=12345678)

@app.route('/params')
def params ():
  args = request.args
  for key, value in args.items():
    print(f"{key}.{value}")
  return args

@app.route('/params_table')
def params_table ():
  args = request.args
  return render_template('params_table.html', args = args)

if __name__ =='__main__':
  app.run(host = '0.0.0.0', port = 5125, threaded = True, debug = True)
#ieej heroku