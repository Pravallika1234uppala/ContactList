#after configuration
#we move to database models.
#first start with data - then can create views that allow to create and modify data.(API are responsible for)

from config import db 
#This is a relative import happening from this config file.
#This instance will give access to SQLAlchemy

class Contact(db.Model):
    #inherits db.model
    #This is a database model represented as python class.
    #Can define diff fields this object will have.
    id = db.Column(db.Integer, primary_key=True) #always present(auto generated)
    #this line means, that this key is used for indexing and should be unique 
    #for every single entry inside the database.
    first_name = db.Column(db.String(80), unique=False, nullable=False) #when specifying String column give maximum length.
    #need to pass first name but can be same.
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #no two contacts can have same email.

    def to_json(self): #this takes all the fields and convert to python dictionary
        #and then can convert dictionary to json(which we can pass from our API)
        #when we build API - we use json to communicate.
        #JSON-Javascript Object Notation (looks like python dictionary)
        #we will send Json back and front. So, API will return json and then we will send json to API for creating different objects.
        return { #returning python dictionary
            #In json- the convention is to have camel case fields while with python we use snake case.
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }




