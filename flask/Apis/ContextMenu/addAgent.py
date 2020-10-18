from flask import request, session, json, make_response
import pymongo

# Database Connection
client = pymongo.MongoClient('mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')
    #mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')
db = client["PerformanceMonitoringSystem"]
col = db.Agents


# Function to add agent machine to db
def addAgent():
    # HTTP Request in JSON
    req = request.json
    print(request.json)

    # Default Response
    res = {
        "code": 401,
        "message": "Authorization Required"
    }
    d = col.find_one({"macAddress": req['macAddress']})

    # Proceed only if the user is admin
    if 'user' in session:
        user = session['user']
        if user['userType'] == 'admin':
            d = col.find_one({"macAddress": req['macAddress']})
            res = {
                "code": 500,
                "message": "Agent addition failed"
            }

            # If the agent machine is not already added, add the agent mac address to database
            if not d:
                up = col.insert_one({
                    "macAddress": req['macAddress'],
                    "refreshTime": 5,
                    "data": []
                })
                print(up)
                if up:
                    res = {
                        "code": 200,
                        "message": "Agent successfully added"
                    }
    print(session)
    response = make_response(json.dumps(res))
    return response
