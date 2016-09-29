from flask import Flask
import sqlite3
from flask import request
import json
app=Flask(__name__)

@app.route('/')
def main():
	return "It's a server!"


@app.route('/login', methods=["GET","POST"])
def login():
	info = request.get_json(force = True)
	userInfo = json.loads(request.get_json(force = True)
	
	sqlite_file = "db/accounts.db"
	table_name = "namePass"
	username_column = "username"
	pass_col = "password"
	usernameIn = userInfo['username']
	passwordIn = userInfo['password']
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute("SELECT * FROM namePass WHERE %s=?" % pass_col,(passwordIn,))
	id_exists = c.fetchone()
	if id_exists:
		print(id_exists[0])
		if id_exists[0] == usernameIn:
			retMessage = {"message" : "You have logged in","code":200}
			
		else:
			retMessage = {"message":"Invalid Log in","code":200}
	else:
		retMessage = {"message":"Invalid Log in","code":200}
	conn.close()
	
	return json.jsonify(retMessage)

