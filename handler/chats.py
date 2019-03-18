from flask import jsonify
from dao.chats import ChatsDAO


class ChatHandler:

    def build_chat_attributes(self, cid, cname, date):
        result = {}
        result['chatId'] = cid
        result['chatName'] = cname
        result['creationDate'] = date
        return result

    def getAllChats(self):
        dao = ChatsDAO()
        chats_list = dao.getAllChats()
        return jsonify(chats_list), 200

    def getChatById(self, cid):
        dao = ChatsDAO()
        chat = dao.getChatById(cid)
        return jsonify(chat), 200

    def searchChats(self, args):
        dao = ChatsDAO()
        chat_list = dao.getChatsByArgs(args)
        return jsonify(chat_list), 200

    def getChatsByMemberId(self, uid):
        dao = ChatsDAO()
        chat_list = dao.getChatsByMemberId(uid)
        return jsonify(chat_list), 200

    def insertChatJson(self, json):
        dao = ChatsDAO()
        newchat = dao.insert(json)
        return jsonify(newchat), 200

    def addContactToChat(self, cid, personid):
        dao = ChatsDAO()
        newmember = dao.addContactToChat(cid, personid)
        return jsonify(newmember), 200

    def updateChat(self, cid, form):
        dao = ChatsDAO()
        updatedchat = dao.update(cid, form)
        return jsonify(updatedchat), 200

    def deleteChat(self, cid):
        dao = ChatsDAO()
        id = dao.delete(cid)
        return jsonify(DeleteStatus = "OK"), 200

    def deleteContactFromChat(self, cid, personid):
        dao = ChatsDAO()
        res = dao.deleteContactFromChat(cid, personid)
        return jsonify(DeleteStatus="OK"), 200







