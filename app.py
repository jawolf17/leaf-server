
from flask import Flask,jsonify,request
import hashlib,json, sqlite3, uuid

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    return "It's a server!"

@app.route('/account-update/<uid>',methods=["POST"])
def account_update(uid):
    #Get request data
    data = request.get_json(force=True)
    #Path to db file
    db_file = "db/server.db"
    #Create Hash Obj
    hasher = hashlib.sha256()
    #connect to db
    con = sqlite3.connect(db_file)
    with con:
        cur = con.cursor()
        #Find User ID
        cur.execute("SELECT password FROM namePass  WHERE id=?",(uid,))
        exists = cur.fetchone()
        #Checks for user existance
        if exists:
            #Check for password match
            hasher.update(data["pass"])
            passw = hasher.hexdigest()
            if  passw == exists[0]:
               #Hash new password if update requested
               if data["password"] != "":
                    hasher2 = hashlib.sha256()
                    hasher2.update(data["password"])
                    passw = hasher2.hexdigest()

               cur.execute("UPDATE namePass SET username=?, password=?, dob=?,phone=?,fName=?, lName=?, bio=? WHERE id=?",
                            (data["username"],passw,data["dob"],data["phone"],data["fName"],data["lName"],data["bio"],uid,))
               return jsonify({"code": 200, "message": "You info has been updated"})
            else:
                return jsonify({"code": 401, "message": "Your password is incorrect"})
        else:
            return jsonify({"code": 403, "message": "User does not exists."})
        #Check for user existance
@app.route('/add-friend/<uid>',methods=["GET","POST"])
def add_freind(uid):
    #Get request data
    data = request.get_json(force=True)
    #Path to file
    db_file = "db/server.db"
    con = sqlite3.connect(db_file)
    with con:
        cur = con.cursor()
        #Find User in DB
        cur.execute("SELECT * FROM namePass WHERE %s=?"%"id",(uid,))
        id_exists = cur.fetchone()
        #Check existance
        if id_exists:
            cur = con.cursor()
            cur.execute("UPDATE namePass SET friendsList=? WHERE id=?",(data["friendsList"],uid,))
            con.commit()
            return jsonify({"code": 200, "message": "Friends List Updated"})
        else:
            return jsonify({"code": 403, "message": "User does not exists"})

@app.route('/login', methods=["GET","POST"])
def login():
    userInfo = request.get_json(force = True)
    #Create HashLib Obj
    hasher = hashlib.sha256()

    sqlite_file = "db/server.db"
    table_name = "namePass"
    username_column = "username"
    pass_col = "password"
    usernameIn = userInfo['username']
    passwordIn = userInfo['password']
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT * FROM namePass WHERE %s=?" % username_column,(usernameIn,))
    id_exists = c.fetchone()
    if id_exists:
        print(id_exists[0])
        #Encode the passowed the user entered
        hasher.update(passwordIn)
        entered = hasher.hexdigest()
        #Get Expected Password
        expected = id_exists[1]

        if entered == expected:
            retMessage = {"message" : "You have logged in","code":200,"username":id_exists[0],"dob":id_exists[2],"phone":id_exists[3],"fName":id_exists[4],"lName":id_exists[5],"currentEvent":id_exists[6],"friendsList":id_exists[7],"bio":id_exists[9],"id":id_exists[10]}
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
    connection = sqlite3.connect('db/server.db')

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
        search = cur.execute("SELECT * FROM namePass WHERE %s=?" % "username",(data["username"],))
        exists = search.fetchone()
        if exists:
            response = {"code": 403, "message": "This Username already exists in the database."}
            return jsonify(response)

        cur.executemany("INSERT INTO namePass VALUES (?,?,?,?,?,?,?,?,?,?,?)", user)
        connection.commit()

    #Create Response
    response = {"message": "A new user has successfully been added to the database. ",
                "code": 200}

    print "[POST] NEW USER CREATION: New user has been added to the database"
    return jsonify(response)



    """
        @Desc: Handles Requests for events
        @Param: id: str- id of event to retrieve
        @Returns: JSON Object containing data and server response codes
    """
@app.route('/get-event/<id>',methods=["GET","POST"])
def get_event(id):
        #Connect to DB
        connection = sqlite3.connect('db/server.db')
        #Initialize Response
        response = {"code": 400, "message": "Could not retreive event."}

        with connection:
            #Query DB for Event
            cur = connection.cursor()
            search = cur.execute("SELECT * FROM events WHERE %s=?" % "id", (id,))
            exists = search.fetchone()
            #If event is found
            if exists:
                #Format Event
                #cols = [description[0] for description in cur.description]
                #event = {key: value for (key,value) in cols}
		event = {'date':exists[0],'time':exists[1],'location':exists[2],'name':exists[3],'description':exists[4],'listofPart':exists[5],'image':exists[6],'owner':exists[7],'arrivalNot':exists[8],'id':exists[9]}
                #Generate Response
                response["code"] = 200
                response["message"] = "Event Retrieved"
                response["event"] = event

        return jsonify(response)

@app.route('/get-user/<username>',methods=["GET","POST"])
def get_user(username):
	connection = sqlite3.connect('db/server.db')
	response = {"code":400,"message":"Could not Retreive user."}

	with connection:
		cur = connection.cursor()
		search = cur.execute("SELECT * FROM namePass WHERE %s=?" % "username",(username,))
		exists = search.fetchone()
		
		if exists:
			user = {'username':exists[0],'dob':exists[2],'phone':exists[3],'fName':exists[4],'lName':exists[5],'friendsList':exists[7],'userPic':exists[8],'bio':exists[9]}
			response['code'] = 200
			response['message'] = "User Retrieved"
			response['user'] = user
	return jsonify(response) 


@app.route('/create-event',methods=["POST"])
def create_event():
    #Get Request
    data = request.get_json(force = True)
    #connect to db
    connection = sqlite3.connect('db/server.db')

    #generate unique id
    u_id = str(uuid.uuid4())



    #format data for insertions
    user = ((data["date"],data["time"],data["location"],data["name"],data["description"],data["listofPart"],data["image"],data["owner"],data["arrivalNot"],u_id),)

    with connection:
        cur = connection.cursor()
        cur.executemany("INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?,?)", user)
        connection.commit()

    #Create Response
    response = {"message": "A new event has successfully been added to the database. ",
                "code": 200}

    print "[POST] NEW EVENT CREATION: New event has been added to the database"
    return jsonify(response)
