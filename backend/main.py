# we will write different routes.
#1. need to figure out all the endpoints and routes you want for API
#(to access diff resources to create resources etc..)
#here, CRUD app:
#Create
#first_name, last_name and email needed. (pass all these)
#read
#update
#delete

#when we create API - we have a server(some kind of address-here, localhost) that runs API
#localhost:5000 - is a domain or server's URL
#like google.com
#endpoint is anything that comes after the domain.(here, home)
#localhost:5000/home

#now, when we hit endpoint/submit request to endpoint we have to submit data along side endpoint.
#here, first name, last name and email.

#Request and Response:
#Request: anything we send to server(kind of)-here,API
#(here we are requesting some thing to happen)
#it has type(can be one of many diff things) but typical ones are:
#1. Get request (to access some type of resource)
#2. Post request (to create something new) like create contact is post request
#3. put or patch request (to update sonething)
#4. Delete request 
#it has json data
#It is the information that comes along side of request.


#so, frontend is gonna send request to backend.
#backend is gonna return a response.
#Response has:
#status - specifies if request is successful.(200) and 404 means not found(if html page or url not rendered)
#400-bad request, 403-formidden or unauthorized.
#these are all diff types of response statuses or codes.(to indicate what happened.)
#can return json.

from flask import request, jsonify
#jsonify - allows us to return json data.
from config import app,db
from models import Contact


#Get method:(will create and specify route and endpoint we go to) and in method specify valid method type(fore that url/route).
@app.route("/contacts", methods=["GET"])  #decorator.
def get_contacts():
    #here we write how to handle get request we sent to route.
    contacts = Contact.query.all()
    #this uses FlaskSQLAlchemy-our ORM to get all contacts from contact database.
    #these contacts are python objects.(can't return python objects from code)
    #can return json data.
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    #contacts -list of contact objects.
    #create a new list that json for the contact by calling to_json
    #map - takes all the elements from the list and apply function and gives result in new list.
    #function used here is called lambda function(function in one line)
    #lambda paramter and call anything using that parameter.
    #so map returns map object but we want list.-list() to convert
    return jsonify({"contacts": json_contacts})#, 200  #success or need not put(default)

#Route for creating contact:
@app.route("/create_contact", methods=["POST"])
def create_contact(): #get data to create
    first_name = request.json.get("firstName") #if key exists returns value or else returns none.
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}), 400,  #bad request
        )
    new_contact = Contact(first_name = first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact) #added to db session(staging area-ready to write to the database)
        db.session.commit() #anything in session is written in database.
    except Exception as e: #catch exception
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201  #craeted

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
#<int:user_id-after passing to the route a number indicating the id of the user that is to be updated.
#looks like /update_contact/76
#then grab the updated info and update the contact.
def update_contact(user_id):
    contact = Contact.query.get(user_id) #finding user in Contact database
    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    #this modifies contact.first_name to firsyName from json data
    #if not found leaves it as it is
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()
    return jsonify({"message": "User updated"}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id) #finding user in Contact database
    if not contact:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message:": "User deleted"}), 200



if __name__ == "__main__": #checks if you are running this file directly
    #if you ran main.py - then execute code below:
    #instances of database:
    with app.app_context(): #gets context of application
        db.create_all() #go and create all (defined)diff models for database
    #Spinning up the Database.
    app.run(debug=True)
    #in python if you import soemthing - it executes all code in that file
    #so, if here protects us to (do soemthing written inside it)




