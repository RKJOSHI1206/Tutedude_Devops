from flask import Flask,request,render_template,jsonify
import json
app = Flask(__name__)

@app.route("/api", methods=['GET'])
def home():
    # Read the JSON file and pass its content to the template
    global j_file
    j_file= open("data.json", "r")
    file_data = json.load(j_file)
    j_file.close()
    return jsonify(file_data)
    #return render_template("index.html",file_data=jsonify(file_data))
"""
@app.route("/api")
def name() :
    name = request.values.get('name')
    age = int(request.values.get('age'))
    name = name.capitalize()
    if age > 18:
        return 'Welcome to the site ' + name +'!'
    else:
        return name+ ' you are too young to use this site!'    
"""

if __name__ == "__main__" :
    app.run(debug=True)
