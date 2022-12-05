from flask import Flask
from flask import Flask,jsonify,request
from urllib.request import urlopen
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():

    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/TESLA?format=json"

    response = requests.get(url)
    jsondata = response.json()

    # Get the JSON response and store it as a Python dict
    my_dictionary = requests.get(url).json()
    #print(json.dumps(my_dictionary, indent=2))
    
    
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
    
