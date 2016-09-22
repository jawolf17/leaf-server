from flask import Flask

app=Flask(__name__)

@app.route('/')
def main():
    return "It's a server!"


@app.route('/login', methods=["GET","POST"])
def login():
    return "LOGIN"
