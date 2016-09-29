from flask import Flask, request
import json, sqlite3, uuid

app=Flask(__name__)

@app.route('/')
def main():
    return "It's a server!"


@app.route('/login', methods=["GET","POST"])
def login():
    return "LOGIN"

@app.route('/create-user',methods=["GET","POST"])
def create_user():
    #Get Request
    data = json.loads(request.get_json(force = True))
    #connect to db
    connection = sqlite3.connect('db/accounts.db')

    #format data for insertions
    user = ((data["username"],data["password"],"","","","","","","",""))

    with connection:
        cur = connection.cursor()
        cur.executeMany("INSERT INTO Cars VALUES (?,?,?,?,?,?,?,?,?,?)", user)
        connection.commit()

    return "Created"
