from pymongo import MongoClient
from flask import request,json,make_response,session
import pyDes

ky="rahul123"

def userAuthentication():
    try:
        client = MongoClient("mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority")
        myDataBase = client["PerformanceMonitoringSystem"]
        myCollection = myDataBase["Users"]
    except Exception:
        return (make_response(json.dumps({"status": "500", "message": "Error in connecting to database!"})))
    req=request.get_json()
    if(req!=None and "authType" in req):
        authType=req["authType"]
        if(authType=="system" and "userName" in req and "password" in req):
            userName=req["userName"]
            pwd=req["password"]
            dic=myCollection.find_one({"authType":authType,"userName":userName})
            if(dic!=None and "password" in dic):
                pwdStored=dic["password"]
            else:
                return (make_response(json.dumps({"status": "500","message":"userName or password not found in database!"})))
            k = pyDes.des(ky, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
            decriptedPwd = k.decrypt(pwdStored)
            if("coord" in dic):
                coord=dic["coord"]
            else:
                coord={}
            if(decriptedPwd.decode("utf-8")==pwd):
                #session[userName+authType]={"userType":"normal"}
                session['user']={"userType":"normal","authType":authType,"userName":userName}
                return(make_response(json.dumps({"status":"202","message":"login successful!","coord":coord})))
            else:
                return(make_response(json.dumps({"status":"401","message":"Credentials do not match!"})))
        elif((authType=="google" and "email" in req)or(authType=="facebook" and "email" in req)):
            email=req["email"]
            dic=myCollection.find_one({"authType":authType,"email":email})
            if(dic!=None):
                if("coord" in dic):
                    coord=dic["coord"]
                else:
                    coord={}
                #session[email + authType] = {"userType": "normal"}
                session["user"]={'userType':"normal","authType":authType,"email":email}
                print(session)
                return(make_response(json.dumps({"status":"200","message":"user exists!","coord":coord})))
            else:
                return(make_response(json.dumps({"status":"401","message":"user not created!"})))
        else:
            return make_response(json.dumps({"status":"400","message":"Bad Request!"}))
    else:
        return(make_response(json.dumps({"status":"400","message":"authType  not provded!"})))