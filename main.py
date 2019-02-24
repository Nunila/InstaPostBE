from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.persons import PersonsHandler
from flask_cors import CORS, cross_origin

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app


# Activate
app = Flask(__name__)

# Apply CORS to this app
CORS(app)


@app.route('/')
@cross_origin()
def greeting():
    return 'Hello, this is the InstaPost DB App!'

#=========================================USERS============================================#

@app.route('/InstaPost/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().getUserByUName(request.args)


@app.route('/InstaPost/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUsersById(uid):
    if request.method == 'GET':
        return UsersHandler().getUserById(uid)
    elif request.method == 'PUT':
        return UsersHandler().updateUser(uid, request.form)
    elif request.method == 'DELETE':
        return UsersHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405



#===============================================PERSONS========================================================#

@app.route('/InstaPost/person', methods=['GET', 'POST'])
def getAllPerson():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PersonsHandler().insertPersonJson(request.json)
    else:
        if not request.args:
            return PersonsHandler().getAllPersons()
        else:
            return PersonsHandler().getPersonByFullName(request.args[0],request.args[1])

@app.route('/InstaPost/person/<int:perid>', methods=['GET', 'PUT', 'DELETE'])
def getPersonByID(perid):
    if request.method == 'GET':
        return PersonsHandler().getPersonById(perid)
    elif request.method == 'PUT':
        return PersonsHandler().updatePerson(perid, request.form)
    elif request.method == 'DELETE':
        return PersonsHandler().deletePerson(perid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/person/email', methods=['GET'])
def getPersonByEmail(permail):
    if request.method == 'GET':
        return PersonsHandler().getPersonByEmail(permail)
    else:
        return jsonify(Error="Method not allowed."), 405

# @app.route('/PartApp/parts/countbypartid')
# def getCountByPartId():
#     return PartHandler().getCountByPartId()


if __name__ == "__main__":
    app.run(port=5000, debug=True)