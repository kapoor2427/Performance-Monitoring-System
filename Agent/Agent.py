# Importing Libraries
from random import randint
import os
import psutil
import requests
import json
import uuid
import re
import time

# URL of the backend server recieving the performance data
serverURL = 'http://127.0.0.1:5000'

# Function to send performance data to server


def sendData():

    # Extracting CPU Usage
    cpuUsageRaw = psutil.cpu_percent(interval=0.1, percpu=True)
    cpuUsage = {}
    for i in range(len(cpuUsageRaw)):
        name = "Core{}".format(i)
        cpuUsage[name] = cpuUsageRaw[i]

    # Extracting Disk Usage
    diskUsage = float(psutil.disk_usage('/').percent)

    # Extracting Memory Usage
    memoryUsage = psutil.virtual_memory().percent

    # Extracting Mac Address
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    print(mac)
    print(memoryUsage)
    print (diskUsage)
    for i in range(len(cpuUsageRaw)):
        print(cpuUsageRaw[i])

    # Initialization
    t = {}
    processes = []
    topCPUUsingProcesses = []
    topMemoryUsingProcesses = []

    # Iterate through processes
    for p in psutil.process_iter():
        try:
            attrs = ['pid', 'name', 'memory_percent', 'cpu_percent']
            t = {attr: p.as_dict()[attr] for attr in attrs}
            t['cpu_percent'] = round(min([t['cpu_percent'], 100]), 3)
            t['memory_percent'] = round(min([t['memory_percent'], 100]), 3)

            processes.append(t)
        except Exception:
            pass

    # Sorting according to memory usage / cpu usage.
        # Top CPU using processes
    topCPUUsingProcesses = sorted(
        processes, key=lambda proc: proc['cpu_percent'], reverse=True)[:5]
    # Top Memory using processes
    topMemoryUsingProcesses = sorted(
        processes, key=lambda proc: proc['memory_percent'], reverse=True)[:5]

    # Building the data
    data = {
        "macAddress": mac,
        "cpuUsage": dict(cpuUsage),
        "memoryUsage": memoryUsage,
        "diskUsage": diskUsage,
        "topMemoryUsingProcesses": topMemoryUsingProcesses,
        "topCPUUsingProcesses": topCPUUsingProcesses
    }
    print(data)

    # Data for refresh time request
    dataRT = {
        "macAddress": mac
    }

    try:
        # HTTP Request to upload performance data to db
        req = requests.post(
            "http://127.0.0.1:5000/api/data",
            json=data)
        
        print(req.json())

        # HTTP Request to get refresh time for the agent machine
        reqRT = requests.get(
            "http://127.0.0.1:5000/api/data/refreshTime",
            json=dataRT)
        res = reqRT.json()
        print(res)

        # Updating Refresh Time
        refreshTime = res['data']

    except Exception:
        # Default
        refreshTime = 5

    return refreshTime


# Setting default interval to 5
refreshTime = 5
latest = int(time.time())

# Infinite Loop to send data after interval = refreshTime
while (True):
    now = int(time.time())

    # If the refresh time interval is over then send the current data
    if now - latest >= refreshTime:
        refreshTime = sendData()
        latest = now
