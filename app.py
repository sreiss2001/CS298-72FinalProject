from flask import Flask
from flask import Flask,jsonify,request
from urllib.request import urlopen
import requests
import json
import random

app = Flask(__name__)

@app.route("/")
def jokeCategories():

    url = "https://api.jokes.one/jod/categories?format=json"

    #Get the JSON response and store it as a Python dict
    my_dictionary = requests.get(url).json()
    my_dictionary["yourNumberTodayIs"] = random.randint(1, 4)
    
    return json.dumps(my_dictionary, indent=2)
  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)



if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)
    
