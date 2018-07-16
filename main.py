#!/usr/bin/python3

from flask import Flask, request, redirect, send_from_directory
import sqlite3, os

filedir = "./uploads/"

app = Flask(__name__)

@app.route("/redir",methods=['GET'])
def app_redir():
	if not 'url' in request.args:
		return "url?", 200
	url = request.args['url']
	return redirect(url)

@app.route("/js",methods=['GET'])
def app_js():
	if 'src' in request.args:
		return "<script src=\"%s\"/>" % request.args['src'], 200
	elif 'script' in request.args:
		return "<script>%s</script>" % request.args['script'], 200
	else:
		return "src?script?", 200

@app.route("/files/<path:path>", methods=['GET'])
def app_file_downl(path):
	return send_from_directory(filedir, path, as_attachment=True)

@app.route("/files/<filename>",methods=['POST'])
def app_file_upl(filename):
	with open(os.path.join(filedir,filename),"wb") as f:
		f.write(request.data)
	return "", 201 # 201 CREATED


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8080)
