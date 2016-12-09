# leaf-server
Server for the LEAF(Locations Events and Friends) Android app.
It contains all methods needed for data handling from the app.
The client code can be found here: https://github.com/jpcerone/eventPlanning

********************************************************
SERVER SET-UP GUIDE

Table of Contents:
I) Run Server Locally
   i) First Time Set-Up
  ii) Run Server
 iii) Troubleshooting
II) Run Server in Baldy 19
   i) First Time Set-Up
  ii) Run Server
 iii) Troubleshooting
********************************************************

NOTE: These instructions were written for Linux.

I) Run Server Locally:

  i) First Time Set-Up:
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

  ii) Run Server
      1) Start Virtual Enviroment
         a) source venv/bin/activate
      2)Run
         a) export FLASK_APP = app.py
         b) flask run

  iii) Troubleshooting
       1) Missing Dependency
          a) Run the requirements install again. See 3b - 3c


II) Run Server in Baldy 19

  i) First Time Set-Up:
     1) Log into Baldy 19 Server
        a) ssh developer@hawkeye.cse.buffalo.edu
        b) enter password (see pinned message on slack, event_app_priv)

     2) Ensure you have dependencies installed
        a) sudo apt-get install python-pip
        b) sudo apt-get install virtualenv
        c) pip install --upgrade virtualenv
        d) sudo apt-get install git

     3) Clone Repo
        a)  git clone https://github.com/jawolf17/leaf-server
        b)  cd leaf-server

     4) Create Virtual Enviroment & install python dependencies
        a) virtualenv venv
        b) source venv/bin/activate
        c) pip install --upgrade -r requirements.txt

     5) Run Server
        a) export FLASK_APP=app.py
        b) flask run --host=0.0.0.0 --port=1032 (http://128.205.44.21:1032/)
        c) Ctrl-C to exit server (server will continue to run)

  ii) Run Server
      1) Start Virtual Enviroment
         a) source venv/bin/activate
      2)Run
         a) export FLASK_APP = app.py
         b) flask run --host=0.0.0.0 --port=1032 (http://128.205.44.21:1032/)

   iii) Troubleshooting
        1) No directories on Server
           a) Someone probably broke the server, and it had to be reset.
              Repeat first time setup.
