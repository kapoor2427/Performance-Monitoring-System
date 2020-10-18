from flask import request,make_response,json,send_file,session
import datetime
from pymongo import MongoClient

client = MongoClient("mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority")
myDataBase = client["PerformanceMonitoringSystem"]
myCollection = myDataBase["Agents"]

def exportData():
    if 'user' in session:
        req=request.args
        print(req)
        if(req!=None and "startDate" in req and "endDate" in req):
            startDate=req["startDate"]
            endDate=req["endDate"]
        else:
            return make_response(json.dumps({"status":"400","message":"Bad request.Either startDate or endDate not given!"}))
        if(startDate==endDate):
            endDate=endDate+" 23:59:59"
        else:
            endDate=endDate+" 00:00:00"

        startTime=int(datetime.datetime.strptime(startDate, "%d-%m-%Y").timestamp())
        endTime=int(datetime.datetime.strptime(endDate, "%d-%m-%Y %H:%M:%S").timestamp())
        fileName="file_"+str(startTime)+"_"+str(endTime)+".csv"
        try:
            fh=open(fileName,"w+")
        except FileNotFoundError:
            return make_response(json.dumps({"status":"500","message":"Error in file creation!"}))
        try:
            max_cores = 0
            st=""
            for i in myCollection.find():
                for j in i["data"]:
                    if (j["timestamp"] >= startTime and j["timestamp"] <= endTime):
                        string = i["macAddress"] + "," + str(j["timestamp"]) + ","
                        count = 0
                        for keys in j["cpuUsage"]:
                            string += str(j["cpuUsage"][keys]) + ","
                            count += 1
                        string += str(j["memoryUsage"]) + "," + str(j["diskUsage"]) + "\n"
                        st+=string
                        if (count > max_cores):
                            max_cores = count
            string2= "MAC_Address" + "," + "TimeStamp" + ","
            for i in range(max_cores):
                string2 += "Core" + str(i) + ","
            string2 += "Memory_Usage" + "," + "Disk_Usage" + "\n"
            st=string2+st
            fh.write(st)
            del st
            fh.close()
            return (make_response(send_file(fileName,as_attachment=True)))
        except Exception:
           return (make_response(json.dumps({"status": "500", "message": "Unsuccessful!"})))
    else:
        return(make_response(json.dumps({"status":"401","message":"Session expired!"})))