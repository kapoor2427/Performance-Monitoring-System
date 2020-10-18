from flask import json,request,make_response,session
from pymongo import MongoClient

client = MongoClient("mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority")
myDataBase = client["PerformanceMonitoringSystem"]
myCollection = myDataBase["Users"]

def nodeCoord():
    if 'user' in session:
        user = session['user']
        try:
            req=request.get_json()
        except Exception:
            return(make_response(json.dumps({"status":"400","message":"JSON request error!"})))
        if ("authType" in user):
            authType = user["authType"]
            if (authType == "system" and "userName" in user and "coord" in req):
                userName = user["userName"]
                coord = req["coord"]
                dic = myCollection.find_one({"authType": authType, "userName": userName})
                if (dic != None):
                    myCollection.update_one({"authType": authType, "userName": userName}, {"$set": {"coord": coord}})
                    return (make_response(json.dumps({"code": "200", "message": "success"})))
                else:
                    return (make_response(json.dumps({"code": "502", "message": "user does not exist in database"})))
            elif (authType == "google" and "email" in user and "coord" in req):
                email = user["email"]
                coord = req["coord"]
                dic = myCollection.find_one({"authType": authType, "email": email})
                if (dic != None):
                    myCollection.update_one({"authType": authType, "email": email}, {"$set": {"coord": coord}})
                    return (make_response(json.dumps({"code": "200", "message": "success"})))
                else:
                    return (make_response(
                        json.dumps({"code": "502", "message": "email user does not exist for authType google in database!"})))
            elif (authType == "facebook" and "email" in user and "coord" in req):
                email = user["email"]
                coord = req["coord"]
                dic = myCollection.find_one({"authType": authType, "email": email})
                if (dic != None):
                    myCollection.update_one({"authType": authType, "email": email}, {"$set": {"coord": coord}})
                    return (make_response(json.dumps({"code": "200", "message": "success"})))
                else:
                    return (make_response(
                        json.dumps({"code": "502", "message": "email user does not exist for authType facebook in database!"})))
            else:
                return (make_response(json.dumps({"status": "404", "message": "value of authType mismatch in session or 'email or userName not found in session'!"})))
        else:
            return (make_response(json.dumps({"code": "502", "message": "authType not found in session!"})))
    else:
        return (make_response(json.dumps({"code": "401", "message": "Session Expired!"})))