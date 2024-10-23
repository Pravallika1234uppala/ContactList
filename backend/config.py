#In config-we are building API first-This happens in Flask.
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#CORS - stands for course origin request
#this helps to send request to backend from a different URL.
#(by default when we send request they are protected)-so server can't be hit from a different URL.

#In our case-front end is different server from backend.
#want front end to communicate with backend.
#So, to make it work we should remove this cors error which pops up.


#This is and ORM(Object relational Mapping)-means modifying SQL using python.

app = Flask(__name__) #This intializes flask application


CORS(app) #warp app in cors to diable that error.

#Now we will be able to send Cross origin requests.

#Database intializations:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

#here we give location of local SQLlite database.(that we store on our machine.)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#this tracks all the modifications to the database.

#creating instance of the database.(it gives access to the database we specified earlier: mydatabase.db)
db = SQLAlchemy(app)

