from flask import Flask, jsonify, request
from handler.users import UsersHandler
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

# =========================================USERS============================================#

@app.route('/InstaPost/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUserss()
        else:
            return UsersHandler().getUserByUName(request.args)


@app.route('/InstaPost/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUsersById(uid):
    if request.method == 'GET':
        return UsersHandler().getUsersById(uid)
    elif request.method == 'PUT':
        return UsersHandler().updateUsers(uid, request.form)
    elif request.method == 'DELETE':
        return UsersHandler().deleteUsers(uid)
    else:
        return jsonify(Error="Method not allowed."), 405



# @app.route('/PartApp/parts/countbypartid')
# def getCountByPartId():
#     return PartHandler().getCountByPartId()


if __name__ == "__main__":
    app.run(port=5000, debug=True)