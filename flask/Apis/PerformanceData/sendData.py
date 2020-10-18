from pymongo import MongoClient
from flask import json, request, make_response, session

client = MongoClient("mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority")
myDataBase = client["PerformanceMonitoringSystem"]
myCollection = myDataBase["Agents"]

def sendData():
    if ("user" in session):
        data = []
        maxCores = 0
        for i in myCollection.find():
            try:
                latestTimestamp = i["latestTimestamp"]
            except KeyError:
                continue
            dic = myCollection.find_one({"_id": i["_id"]}, {"data": {"$elemMatch": {"timestamp": latestTimestamp}}})
            dic["macAddress"] = i["macAddress"]
            if ("data" not in dic):
                while True:
                    latestTimestamp -= 1
                    if (latestTimestamp <= 0):
                        return make_response(json.dumps({"status": "500",
                                                         "message": "latestTimestamp value reached negetive while searching in the database."}))
                    dic = myCollection.find_one({"_id": i["_id"]},
                                                {"data": {"$elemMatch": {"timestamp": latestTimestamp}}})
                    if ("data" not in dic):
                        continue
                    else:
                        break
            del dic["_id"]
            del dic["data"][0]["timestamp"]
            s = 0
            l = 0
            for c in dic["data"][0]["cpuUsage"]:
                s += dic["data"][0]["cpuUsage"][c]
                l += 1
            avg = s / l
            dic["data"][0]["cpuUsageTotal"] = round(avg,3)
            if l > maxCores:
                maxCores = l
            obj = dic["data"][0]
            obj['macAddress'] = dic["macAddress"]
            obj['latestTimestamp'] = latestTimestamp
            obj['refreshTime'] = i['refreshTime']
            data.append(obj)
        res = {'status': '200', 'data': data, "maxCores": maxCores}
        print(res)
        response = make_response(json.dumps(res))
        return response
    else:
        return (make_response(json.dumps({"status": "401", "message": "User Un-Authorised or session expired!"})))
