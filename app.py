import flask
import os.path
app = flask.Flask(__name__)

@app.route("/")
@app.route("/<path:rest>")
def main(rest=None):
	out = '<!DOCTYPE html>\n<html>\n<head lang="en">\n\t<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<title>Backend Server HTTP header print</title>\n\t<style>\n\t\tbody {\n\t\t\tbackground-color: #282828;\n\t\t\tfont-family:"Courier New", Courier, monospace\n\t\t}\n\t\ttable {\n\t\t\twidth: auto;\n\t\t}\n\t\tth {\n\t\t\ttext-align: left;\n\t\t\tcolor: #ffb000;\n\t\t}\n\t\ttd {\n\t\t\tcolor:#ffb000;\n\t\t}\n\t\ttr:hover {\n\t\t\tbackground-color: #1c1506d8;\n\t\t}\n\t\ttr {\n\t\t\tborder-bottom: 1cm solid #000000;\n\t\t\tpadding-right: 5cm;\n\t\t}\n\t</style>\n</head>\n<body>\n\t<section style="background-color:#fff">\n\t\t<div class="container">\n\t\t<div class="row">\n\t\t\t<br>\n\t\t\t<h2> Backend Server HTTP header print</h2>\n\t\t\t<br>\n\t\t</div>\n\t\t</div>\n\t</section>\n\t<div class="content">\n\t\t<div class="content-text">\n\t\t\t<table>\n\t\t\t<tr>\n\t\t\t\t<th>Header name</th>\n\t\t\t\t<th>Header value</th>\n\t\t\t</tr>'
	for value in flask.request.headers.keys():
		out += '\n\t\t\t<tr>'
		out += '\n\t\t\t\t<td>' + value + '</td>'
		out += '\n\t\t\t\t<td> ' + flask.request.headers[value] + ' </td>'
		out += '\n\t\t\t</tr>'
	out += '\n\t\t</div>\n\t</div>\n</body></html>'
	path = flask.request.url.split('/')
	if('User-Agent' not in flask.request.headers.keys() or flask.request.headers['User-Agent'] == None or flask.request.headers['User-Agent'] == 'Edge Health Probe'):
		file = open('healthprobe.txt', 'w')
		file.write(out)
		file.close()
	if(path[3].isdigit()):
		status = int(path[3])
		if(status >= 400):
			flask.abort(status)
		else:
			return(out, status)
	elif(path[3] == 'healthprobe'):
		if(os.path.exists('healthprobe.txt')):
			try:
				file = open('healthprobe.txt')
				out = file.read()
			finally:
				file.close()
			return(out)
		else:
			return('No Health Probe yet')
	else:
		return(out)
