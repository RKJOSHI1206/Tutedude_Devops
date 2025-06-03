from flask import Flask,request,render_template
from dotenv import load_dotenv
import os
import json
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
app = Flask(__name__)
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db=client.get_database("test_db")
# Create a collection
collection = db["flask-tutorial"]
# Define the home route  
@app.route("/")
def home():
   return render_template("index.html")
# Define the register route
@app.route("/register", methods=['POST'])
def register():
    # Get the data from the form
    name = request.form.get('name')
    pwd = request.form.get('password')
    collection.insert_one({"name": name, "password": pwd})
    return ("Data submitted successfully!")

@app.route("/submittodoitem", methods=['POST'])
def submittodoitem():
    # Get the data from the form
    item_name = request.form.get('item_name')
    item_desc= request.form.get('item_desc')
    todoitem = {"name": item_name, "description": item_desc}
    collection.insert_one({"todoitem": todoitem})
    return ("Todo item submitted successfully!")

if __name__ == "__main__" :
    app.run(debug=True)
