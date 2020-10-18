from flask import request, json
import pymongo
import time

# Database Connection
client = pymongo.MongoClient('mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')
db = client["PerformanceMonitoringSystem"]
col = db.Agents


# Function to collect req from agent machines and store it in the database
def postData():
    req = request.json
    print(req)
    # Default Response
    res = {
        "code": 500,
        "message": "Data upload failed"
    }

    d = col.find_one({"macAddress": req['macAddress']})
    mac = req.pop('macAddress')
    req['timestamp'] = int(time.time())

    # If the agent machine is allowed to post data
    if d != None:
        up = col.update_one({"macAddress": mac},
                            {'$push': {
                                'data': req
                            }})
        col.update_one({"macAddress": mac},
                       {'$set': {
                           'latestTimestamp': req['timestamp']
                       }})
        print(req)
        if up:
            res = {
                "code": 200,
                "message": "Data Upload Successful"
            }

    return json.dumps(res)
