
from flask import Flask,jsonify,request
import hashlib,json, sqlite3, uuid

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    return "It's a server!"


@app.route('/login', methods=["GET","POST"])
def login():
    userInfo = request.get_json(force = True)

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
            retMessage = {"message":"Invalid Log in","code":403}
    else:
        retMessage = {"message":"Invalid Log in","code":403}

    conn.close()
    return jsonify(retMessage)

@app.route('/create-user',methods=["POST"])
def create_user():
    #Get Request
    data = request.get_json(force = True)
    print data["username"]
    #connect to db
    connection = sqlite3.connect('db/accounts.db')

    #generate unique id
    u_id = str(uuid.uuid4())

    #Create Hash Object
    hasher = hashlib.sha256()
    #Hash the password
    hasher.update(data["password"])
    data["password"] = hasher.hexdigest()
    #format data for insertions
    user = ((data["username"],data["password"],"","","","","","","","",u_id),)

    with connection:
        cur = connection.cursor()
        cur.executemany("INSERT INTO namePass VALUES (?,?,?,?,?,?,?,?,?,?,?)", user)
        connection.commit()

    #Create Response
    response = {"message": "A new user has successfully been added to the database. ",
                "code": 200}

    print "[POST] NEW USER CREATION: New user has been added to the database"
    return jsonify(response)
