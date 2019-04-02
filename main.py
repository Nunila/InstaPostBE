from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handler.persons import PersonsHandler
from handler.users import UsersHandler
from handler.chats import ChatHandler
from handler.reactions import ReactionHandler
from handler.posts import PostHandler
from handler.hashtag import HashtagHandler
from handler.messages import MessageHandler
from handler.contact import ContactHandler
from handler.participates import ParticipatesHandler


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
        return UsersHandler().getAllUsers()

@app.route('/InstaPost/users/<string:uname>', methods=['GET'])
def getUsersByUname(uname):
    if request.method == 'GET':
        return UsersHandler().getUserByUName(uname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUsersById(uid):
    if request.method == 'GET':
        return UsersHandler().getUserByID(uid)
    elif request.method == 'PUT':
        return UsersHandler().updateUser(uid, request.form)
    elif request.method == 'DELETE':
        return UsersHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/users/mostactive', methods=['GET'])
def getMostActiveUser():
    if request.method == 'GET':
        return UsersHandler().getMostActiveUser()
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/users/chat/<int:cid>', methods=['GET'])
def getUsersInSpecificChat(cid):
    if request.method == 'GET':
        return ParticipatesHandler().getUsersInSpecificChat(cid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/users/chatowner/<int:cid>', methods=['GET'])
def getOwnerInSpecificChat(cid):
    if request.method == 'GET':
        return ParticipatesHandler().getOwnerInSpecificChat(cid)
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
            return PersonsHandler().getPersonByArguments(request.args)


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


@app.route('/InstaPost/person/<int:ownerid>/contacts', methods=['GET'])
def getContactsOfPerson(ownerid):
    if request.method == 'GET':
        return ContactHandler().getContactsOfPerson(ownerid)
    else:
        return jsonify(Error="Method not allowed."), 405

# -----------------------------------CHATS------------------------------------------


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


@app.route('/InstaPost/chats/<int:cid>/member/<int:personid>', methods=['POST', 'DELETE'])
def addPersonToChat(cid, personid):
    if request.method == 'POST':
        return ChatHandler().addContactToChat(cid, personid)
    elif request.method == 'DELETE':
        return ChatHandler().deleteContactFromChat(cid, personid)
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
            return ReactionHandler().getAllReactionsForMessages()
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


@app.route('/InstaPost/reactions/countlikes/<string:date>', methods=['GET'])
def getLikesByDate(date):
    if request.method == 'GET':
        return ReactionHandler().getLikesCountOnDate(date)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/reactions/countdislikes/<string:date>', methods=['GET'])
def getDislikesByDate(date):
    if request.method == 'GET':
        return ReactionHandler().getDislikesCountOnDate(date)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/reactions/<int:postId>/likes', methods=['GET'])
def getLikesOfPost(postId):
    if request.method == 'GET':
        return ReactionHandler().getLikesOfPost(postId)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/reactions/<int:postId>/dislikes', methods=['GET'])
def getDislikesOfPost(postId):
    if request.method == 'GET':
        return ReactionHandler().getDislikesOfPost(postId)
    else:
        return jsonify(Error="Method not allowed."), 405

# --------------------------POSTS-----------------------------------------

@cross_origin()
@app.route('/InstaPost/posts', methods=['GET', 'POST'])
def getAllPosts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPost(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()
        else:
            return jsonify(Result="Search result")


@app.route('/InstaPost/posts/<int:postId>', methods=['GET', 'PUT', 'DELETE'])
def getPostById(postId):
    if request.method == 'GET':
        return PostHandler().getPostById(postId)
    elif request.method == 'PUT':
        return PostHandler().updatePost(postId, request.form)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(postId)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/posts/chat/<int:chatId>', methods=['GET'])
def getPostsByChatId(chatId):
    if request.method == 'GET':
        return PostHandler().getPostsByChatId(chatId)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/posts/user/<int:userId>', methods=['GET'])
def getPostsByUserId(userId):
    if request.method == 'GET':
        return PostHandler().getPostsByUserId(userId)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/posts/postDate/<string:postDate>', methods=['GET'])
def getPostsByDate(postDate):
    if request.method == 'GET':
        return PostHandler().getPostsByDate(postDate)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/posts/numberOfPosts/<string:date>', methods=['GET'])
def getNumOfPostsByDate(date):
    if request.method == 'GET':
        return PostHandler().getNumOfPostsByDate(date)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/posts/numberOfPosts/<string:date>/<int:userId>', methods=['GET'])
def getNumOfPostsByDateAndUser(date, userId):
    if request.method == 'GET':
        return PostHandler().getNumOfPostsByDateAndUser(date, userId)
    else:
        return jsonify(Error="Method not allowed."), 405

# ------------------------MESSAGES-------------------------------------------


@app.route('/InstaPost/messages', methods=['GET', 'POST'])
def getAllMessages():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return MessageHandler().insertMessage(request.json)
    else:
        if not request.args:
            return MessageHandler().getAllMessages()
        else:
            return jsonify(Result="Search result")


@app.route('/InstaPost/messages/<int:messageId>', methods=['GET', 'PUT', 'DELETE'])
def getMessageById(messageId):
    if request.method == 'GET':
        return MessageHandler().getMessageById(messageId)
    elif request.method == 'PUT':
        return MessageHandler().updateMessage(messageId, request.form)
    elif request.method == 'DELETE':
        return MessageHandler().deleteMessage(messageId)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/messages/post/<int:postId>', methods=['GET', 'PUT', 'DELETE'])
def getMessageByPostId(postId):
    if request.method == 'GET':
        return MessageHandler().getMessagesByPostId(postId)
    elif request.method == 'PUT':
        return MessageHandler().updateMessage(postId, request.form)
    elif request.method == 'DELETE':
        return MessageHandler().deleteMessage(postId)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/messages/user/<int:userId>', methods=['GET', 'PUT', 'DELETE'])
def getMessageByUserId(userId):
    if request.method == 'GET':
        return MessageHandler().getMessagesByUserId(userId)
    elif request.method == 'PUT':
        return MessageHandler().updateMessage(userId, request.form)
    elif request.method == 'DELETE':
        return MessageHandler().deleteMessage(userId)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/messages/messageDate/<string:messageDate>', methods=['GET'])
def getMessageByDate(messageDate):
    if request.method == 'GET':
        return MessageHandler().getMessagesByUserId(messageDate)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/messages/numberOfReplies/<string:date>', methods=['GET'])
def getNumOfRepliesByDate(date):
    if request.method == 'GET':
        return MessageHandler().getNumOfRepliesByDate(date)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/messages/numberOfReplies/<string:date>/<int:postId>', methods=['GET'])
def getNumOfRepliesByDateAndPost(date, postId):
    if request.method == 'GET':
        return MessageHandler().getNumOfRepliesByDateAndPost(date, postId)
    else:
        return jsonify(Error="Method not allowed."), 405


# ---------------------------- HASHTAGS --------------------------------

@app.route('/InstaPost/hashtags', methods=['GET', 'POST'])
def getAllHashtags():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return HashtagHandler().insertHashtagJson(request.json)
    else:
        if not request.args:
            return HashtagHandler().getAllHashtags()
        else:
            return HashtagHandler().searchHashtags(request.args)


@app.route('/InstaPost/hashtags/<int:hid>', methods=['GET', 'PUT', 'DELETE'])
def getHashtagId(hid):
    if request.method == 'GET':
        return HashtagHandler().getHashtagById(hid)
    elif request.method == 'PUT':
        return HashtagHandler().updateHashtag(hid, request.form)
    elif request.method == 'DELETE':
        return HashtagHandler().deleteHashtag(hid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaPost/hashtags/trending', methods=['GET'])
def getTrendingHash():
    if request.method == 'GET':
        return HashtagHandler().getTrendingHash()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
