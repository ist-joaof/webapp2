from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
	out = ''
	for line in request.headers:
		out += '<p>' + str(line) + '</p>'
	return(out)
