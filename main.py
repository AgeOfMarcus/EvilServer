#!/usr/bin/python3

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/redir",methods=['GET'])
def app_redir():
	if not 'url' in request.args:
		return "url?", 200
	url = request.args['url']
	return redirect(url)




if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8080)
