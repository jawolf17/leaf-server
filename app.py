from flask import Flask, request
import json, sqlite3, uuid

app=Flask(__name__)

@app.route('/')
def main():
    return "It's a server!"


@app.route('/login', methods=["GET","POST"])
def login():
    return "LOGIN"

@app.route('/create-user',methods=["POST"])
def create_user():
    #Get Request
    data = json.loads(request.get_json(force = True))
    #connect to db
    connection = sqlite3.connect('db/accounts.db')

    #generate unique id
    u_id = str(uuid.uuid4())

    #format data for insertions
    user = ((data["username"],data["password"],"","","","","","","","",u_id),)

    with connection:
        cur = connection.cursor()
        cur.executeMany("INSERT INTO namePass VALUES (?,?,?,?,?,?,?,?,?,?)", user)
        connection.commit()

    #Create Response
    response = {"message": "A new user has successfully been added to the database. ",
                "code": 200}

    print "[POST] NEW USER CREATION: New user has been added to the database"
    return json.jsonify(response)
