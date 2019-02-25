from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.persons import PersonsHandler
from flask_cors import CORS, cross_origin
from handler.chats import ChatHandler
from handler.reactions import ReactionHandler
from handler.posts import PostHandler
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


# ===============================================PERSONS========================================================#


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

# -----------------------------CHATS----------------------------------


@app.route('/InstaPost/chats', methods=['GET', 'POST'])
def getAllChats():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().insertChatJson(request.json)
    else:
        if not request.args:
            return ChatHandler().getAllChats()
        else:
            return ChatHandler().searchChats(request.args)


@app.route('/InstaPost/chats/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def getChatById(cid):
    if request.method == 'GET':
        return ChatHandler().getChatById(cid)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(cid, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(cid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/chats/<int:uid>/member', methods=['GET'])
def getChatByMemberId(uid):
    if request.method == 'GET':
        return ChatHandler().getChatsByMemberId(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

# ---------------------------REACTIONS--------------------------------


@app.route('/InstaPost/reactions', methods=['GET', 'POST'])
def getAllReactions():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReactionHandler().insertReactionJson(request.json)
    else:
        if not request.args:
            return ReactionHandler().getAllReactions()
        else:
            return ReactionHandler().searchReactions(request.args)


@app.route('/InstaPost/reactions/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getReactionById(rid):
    if request.method == 'GET':
        return ReactionHandler().getReactionById(rid)
    elif request.method == 'PUT':
        return ReactionHandler().updateReaction(rid, request.form)
    elif request.method == 'DELETE':
        return ReactionHandler().deleteReaction(rid)
    else:
        return jsonify(Error="Method not allowed."), 405


# --------------------------POSTS-----------------------------------------


@app.route('/InstaPost/posts', methods=['GET', 'POST'])
def getAllPosts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPost(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()
#         else:
#             return ReactionHandler().searchReactions(request.args)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
