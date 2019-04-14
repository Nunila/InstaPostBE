from flask import jsonify
from dao.chats import ChatsDAO


class ChatHandler:

    def buildChatDict(self, row):
        result = {}
        result['chatId'] = row[0]
        result['chatName'] = row[1]
        result['creationDate'] = row[2]
        result['ownerId'] = row[3]
        return result

    def build_chat_attributes(self, cid, cname, date):
        result = {}
        result['chatId'] = cid
        result['chatName'] = cname
        result['creationDate'] = date
        return result

#--------------------Operations-----------------------------------------

    def getAllChats(self):
        dao = ChatsDAO()
        chats_List = dao.getAllChats()
        result_list = []
        for row in chats_List:
            result = self.buildChatDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getChatById(self, cid):
        dao = ChatsDAO()
        row = dao.getChatById(cid)
        if not row:
            return jsonify(Error="Part Not Found"), 404
        else:
            part = self.buildChatDict(row)

        return jsonify(Chat=part)

    def getAllPostsOfSpecificChat(self, cid):
        dao = ChatsDAO()
        chats_List = dao.getAllChats()
        result_list = []
        for row in chats_List:
            result = self.buildChatDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getChatsByParticipatingId(self, uid):
        dao = ChatsDAO()
        chats_List = dao.getChatsByParticipatingId(uid)
        result_list = []
        for row in chats_List:
            result = self.buildChatDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def searchChats(self, args):
        dao = ChatsDAO()
        chat_list = dao.getChatsByArgs(args)
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







