# leaf-server
Server for the LEAF(Locations Events and Friends) Android app.
It contains all methods needed for data handling from the app.

********************************************************
SERVER SET-UP GUIDE

Table of Contents:
   I) First Time Set-Up
  II) Run Server
 III) Troubleshooting
********************************************************

NOTE: These instructions were written Linux.

I) First Time Set-Up:
     1) Ensure you have dependencies installed
	      a)sudo apt-get install python-pip
        b) sudo apt-get install virtualenv
        c) sudo apt-get install git

     2) Clone Repo
        a)  git clone https://github.com/jawolf17/leaf-server
        b)  cd leaf-server

     3) Create Virtual Enviroment & install python dependencies
        a) virtualenv venv
        b) source venv/bin/activate
        c) pip install -r requirements.txt

     4) Run Server
        a) export FLASK_APP=app.py
        b) flask run

II) Run Server
    1) Start Virtual Enviroment
       a) source venv/bin/activate
    2)Run
       a) export FLASK_APP = app.py
       b) flask run

III) Troubleshooting
     1) Missing Dependency
        a) Run the requirements install again. See 3b - 3c
