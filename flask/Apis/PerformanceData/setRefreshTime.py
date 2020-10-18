# Author : Sarthak Sengupta
# Created on 20 July 2019

from flask import request, session, json
import pymongo

# Database Connection
client = pymongo.MongoClient("mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority")
db = client["PerformanceMonitoringSystem"]
col = db.Agents


# Function to set the refresh time for the agent machines
def setRefreshTime():
    req = request.json

    # Default Response
    res = {
        "code": 500,
        "message": "Error"
    }
    d = col.find({"macAddress": req['macAddress']}).count()

    # If the agent machine is allowed to update refresh time on database
    if d != 0:
        res = {
            "code": 401,
            "message": "Authorization Required"
        }
        if 'user' in session:
            user = session['user']
            if user['userType'] == 'admin':
                rt = col.update({"macAddress": req['macAddress']},
                                {"$set":
                                     {"refreshTime": req['refreshTime']}
                                 })
                res = {
                    "code": 200,
                    "message": "Refresh Time setting successful",
                }

    return json.dumps(res)
