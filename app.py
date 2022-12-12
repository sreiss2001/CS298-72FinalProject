from flask import Flask
from flask import Flask,jsonify,request
from urllib.request import urlopen
import requests
import json
import random

app = Flask(__name__)

@app.route("/")
def jokeCategories():
    #contains my API key
    headers = {
        'X-Api-Key' : '1c81aafe3e504962b5c9c34f2c4c56fb'
    }
    
    #performs a get request to specified url
    req = requests.get("https://randommer.io/api/Name?nameType=firstname&quantity=1", headers=headers)
    req = req.json()

    #creates a dictionary which contains the generated random name
    myDict = {
        "yourRandomName" : req[0]
    }
    
    return json.dumps(myDict, indent=2)

if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)
    
