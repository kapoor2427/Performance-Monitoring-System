from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from Apis.Authentication.adminAuth import adminAuth
from Apis.Authentication.adminAuth import adminLogout
from Apis.PerformanceData.postData import postData
from Apis.ContextMenu.addAgent import addAgent
from Apis.ContextMenu.deleteAgent import deleteAgent
from Apis.PerformanceData.getRefreshTime import getRefreshTime
from Apis.PerformanceData.setRefreshTime import setRefreshTime

from Apis.PerformanceData.sendData import sendData
from Apis.PerformanceData.exportData import exportData
from Apis.Authentication.createUser import createUser
from Apis.Authentication.userLogout import userLogout
from Apis.Authentication.userAuthentication import userAuthentication
from Apis.PerformanceData.nodeCoord import nodeCoord

#Instatiatite Flask App
app = Flask(__name__)

cors = CORS(app, origins=["*"], headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'],
            supports_credentials=True)

app.secret_key = "secretkey"

app.add_url_rule(rule='/api/auth/admin', methods=['POST'], endpoint='adminAuth', view_func=adminAuth)
app.add_url_rule(rule='/api/auth/admin/logout', methods=['POST'], endpoint='adminLogout', view_func=adminLogout)
app.add_url_rule(rule='/api/data', methods=['POST'], endpoint='extractData', view_func=postData)
app.add_url_rule(rule='/api/data/refreshTime', methods=['GET'], endpoint='getRefreshTime', view_func=getRefreshTime)
app.add_url_rule(rule='/api/menu/add', methods=['POST'], endpoint='menuAdd', view_func=addAgent)
app.add_url_rule(rule='/api/menu/delete', methods=['POST'], endpoint='Delete', view_func=deleteAgent)
app.add_url_rule(rule='/api/data/refreshTime', methods=['POST'], endpoint='setRefreshTime', view_func=setRefreshTime)

app.add_url_rule(rule='/api/data', methods=['GET'], endpoint='sendData', view_func=sendData)
app.add_url_rule(rule='/api/data/export', methods=['GET'], endpoint='exportData', view_func=exportData)
app.add_url_rule(rule='/api/auth/user/create', methods=['POST'], endpoint='createUser', view_func=createUser)
app.add_url_rule(rule='/api/auth/user', methods=['POST'], endpoint='userAuthentication', view_func=userAuthentication)
app.add_url_rule(rule='/api/auth/user/logout', methods=['POST'], endpoint='userLogout', view_func=userLogout)
app.add_url_rule(rule='/api/data/coordinates', methods=['POST'], endpoint='nodeCoord', view_func=nodeCoord)


app.config['MONGO_URI'] = "mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority"
#mongodb+srv://swadha:QWERTYqwerty@cluster0-40htb.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route("/")
def index():
	return "Server Running"

if __name__ == '__main__':
	app.run(debug=True)