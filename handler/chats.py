from flask import jsonify
from dao.chats import ChatsDAO


class ChatHandler:

    def build_chat_attributes(self, cid, cname, cowner, date):
        result = {}
        result['chatId'] = cid
        result['chatName'] = cname
        result['chatOwnerId'] = cowner
        result['creationDate'] = date
        return result

#-------------------------Modifications-----------------------------
    def getAllChats(self):
        dao = ChatsDAO()
        chats_list = dao.getAllChats()
        return jsonify(chats_list)

    def getChatById(self, cid):
        dao = ChatsDAO()
        chat = dao.getChatById(cid)
        return jsonify(chat)

    def searchChats(self, args):
        dao = ChatsDAO()
        chat_list = dao.getChatsByArgs(args)
        return jsonify(chat_list)

    def getChatsByMemberId(self, uid):
        dao = ChatsDAO()
        chat_list = dao.getChatsByMemberId(uid)
        return jsonify(chat_list)

    def insertChatJson(self, json):
        dao = ChatsDAO()
        newchat = dao.insert(json)
        return jsonify(newchat)

    def updateChat(self, cid, form):
        dao = ChatsDAO()
        updatedchat = dao.update(cid, form)
        return jsonify(updatedchat)

    def deleteChat(self, cid):
        dao = ChatsDAO()
        id = dao.delete(cid)
        return jsonify(DeleteStatus = "OK"), 200








