import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
	out = ''
	for line in flask.request.headers:
		out += '<p>' + str(line) + '</p>'
	return(out)
