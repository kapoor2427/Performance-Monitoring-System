from flask import request, session, json
import pymongo

# Database Connection
client = pymongo.MongoClient('mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')
db = client["PerformanceMonitoringSystem"]
col = db.Agents


# Function to get the refresh time for the agent machines
def getRefreshTime():

    req = request.json

    # Default Response
    res = {
        "code": 500,
        "message": "Error"
    }
    d = col.find({"macAddress": req['macAddress']}).count()

    # If the agent machine is allowed to upload data push data to database
    if d != 0:
        rt = col.find_one({"macAddress": req['macAddress']}, {"refreshTime": 1})
        res = {
            "code": 200,
            "message": "Refresh Time extraction successful",
            "data": int(rt['refreshTime'])
        }

    return json.dumps(res)
