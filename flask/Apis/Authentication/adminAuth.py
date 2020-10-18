# import pam
import json
import platform
from flask import request, session, json, jsonify, make_response, redirect
from pymongo import MongoClient


client = MongoClient('mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')
    #mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority')


# Function to authenticate admin user
def adminAuth():
    pltfm = platform.system()
    username = request.json['username']
    password = request.json['password']

    # Default Response
    res = {
        "code": 500,
        "message": "Authentication Failed",
    }

    # If the server is on Windows OS
    if pltfm == 'Windows':
        import getpass
        import win32security
        domain = ''
        try:
            User = win32security.LogonUser(
                username,
                domain,
                password,
                win32security.LOGON32_LOGON_NETWORK,
                win32security.LOGON32_PROVIDER_DEFAULT
            )
        except win32security.error:
            res = {
                "code": 500,
                "message": "Authentication Failed"
            }
        else:
            session['user'] = {
                "userType": "admin",
                "username": username
            }
            res = {
                "code": 200,
                "message": "Authentication Successful"
            }


    # If the server is on Linux OS
    elif pltfm == 'Linux':
        res = {
            "code": 500,
            "message": "Authentication Failed"
        }
        rs = pam.pam().authenticate(username, password)
        if rs:
            session['user'] = {
                "userType": "admin",
                "username": username
            }
            res = {
                "code": 200,
                "message": "Authentication Successful",
            }
            print(request.user_agent)
    else:
        res = {
            "code": 500,
            "message": "Server OS Error",
        }
    print(session)
    response = make_response(json.dumps(res))
    return response


# Function to log out admin
def adminLogout():
    # Default Response
    res = {
        "code": 500,
        "message": "Admin Logout Failed"
    }

    # Removing user from Session
    if "user" in session:
        session.pop("user")
        res["code"] = 200
        res["message"] = "Admin Logged out"
            
    print(session)
    response = make_response(json.dumps(res))
    return response
