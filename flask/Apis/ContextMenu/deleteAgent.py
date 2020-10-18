from flask import request, session, json, make_response
import pymongo

# Database Connection
client = pymongo.MongoClient('mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')
db = client["PerformanceMonitoringSystem"]
col = db.Agents


# Function to delete agent nodes from the database
def deleteAgent():
    req = request.json
    print(req)

    # Default Response
    res = {
        "code": 401,
        "message": "Deletion of agent requires authorization"
    }

    # Only for Testing
    d = col.find_one({"macAddress": req['macAddress']})
    res = {
        "code": 500,
        "message": "Agent deletion failed"
    }

    # If the agent machine is added, delete the agent mac address to database
    if d:
        up = col.remove({"macAddress": req['macAddress']})
        print(up)
        if up:
            res = {
                "code": 200,
                "message": "Agent successfully deleted"
            }

    # Proceed only if the user is admin
    # if 'user' in session:
    #     user = session['user']
    #     if user['userType'] == 'admin':
    #         d = col.find_one({"macAddress": req['macAddress']})
    #         res = {
    #             "code": 500,
    #             "message": "Agent deletion failed"
    #         }
    #
    #         # If the agent machine is added, delete the agent mac address to database
    #         if d:
    #             up = col.remove({"macAddress": req['macAddress']})
    #             print(up)
    #             if up:
    #                 res = {
    #                     "code": 200,
    #                     "message": "Agent successfully deleted"
    #                 }

    response = make_response(json.dumps(res))
    return response
