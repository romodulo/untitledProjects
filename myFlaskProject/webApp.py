from flask import Flask, render_template#, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', indexString="Title: None ")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#
#
# I created a second html file to:

# Notes
#
# From the documentation:
# To access parameters submitted in the URL (?key=value) you can use the args attribute::
# searchword = request.args.get('key', '')
#
#

#Notes:
# if request.method == 'POST':
#   do_this()


#
#flask --app webApp run

# the flag --debug at the end
# of the command can
# run the server in debug 
# mode.
