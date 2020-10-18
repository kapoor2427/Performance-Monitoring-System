from flask import session,make_response,json
def userLogout():
    """req=request.get_json()
    if(req!=None and "authType" in req):
        if("userName" in req):
            try:
                session.pop(req["userName"]+req["authType"])
            except KeyError:
                return (make_response(json.dumps({"status": "500", "message": "logout unsuccessful for user " + req["userName"] + "!"})))
            else:
                return (make_response(json.dumps({"status": "200", "message": "User " + req["userName"] + " is logged out successfully!"})))
        elif("email" in req):
            try:
                session.pop(req["email"]+req["authType"])
            except KeyError:
                return (make_response(json.dumps({"status": "500", "message": "logout unsuccessful for "+req["authType"]+" user " + req["userName"] + "!"})))
            else:
                return (make_response(json.dumps({"status": "200", "message": req["authType"]+" user " + req["email"] + " is logged out successfully!"})))
        else:
            return(make_response(json.dumps({"status": "500", "message": "userName or email not provided"})))
    else:
        return(make_response(json.dumps({"status": "500", "message": "authType not provided"})))"""
    try:
        session.pop('user')
        print(session)
    except KeyError:
        return(make_response(json.dumps({"code": 500, "message": "logout unsuccessful!"})))
    else:
        return(make_response(json.dumps({"code": 200, "message": "logout successful!"})))