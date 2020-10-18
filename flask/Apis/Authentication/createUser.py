from pymongo import MongoClient
from flask import request,json,make_response
import pyDes


client = MongoClient("mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority")
myDataBase = client["PerformanceMonitoringSystem"]
myCollection = myDataBase["Users"]

def createUser():
    req=request.get_json()
    if(req != None and "authType" in req):
        authType=req["authType"]
    else:
        return(make_response(json.dumps({"status":"400","message":"Authentication type not provided!"})))
    if(authType=="system"):
        if("userName" in req and "password" in req):
            userName=req["userName"]
            if(myCollection.find_one({"userName":userName})==None):
                pwd=req["password"]
                k = pyDes.des(ky, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
                cipherPwd=k.encrypt(pwd)
                dic={"authType":authType,"userName":userName,"password":cipherPwd}
                myCollection.insert_one(dic)
                return(make_response(json.dumps({"status":"201","message":"user created successfully!"})))
            else:
                return make_response(json.dumps({"status":"403","message":"userName Already exists!"}))
        else:
            return (make_response(json.dumps({"status": "400", "message": "userName or password not provided!"})))
    elif(authType=="google" or authType=="facebook"):
        if("email" in req):
            email=req["email"]
            if(myCollection.find_one({"authType":authType,"email":email})==None):
                dic={"authType":authType,"email":email}
                myCollection.insert_one(dic)
                return (make_response(json.dumps({"status": "201", "message": "user created successfully!"})))
            else:
                return make_response(json.dumps({"status":"400","message":"email already exists!"}))
        else:
            return(make_response(json.dumps({"status": "400", "message": "email not provided!"})))
    else:
        return (make_response(json.dumps({"status": "400", "message": "Authentication type must be either 'system' or 'google' or 'facebook'"})))

