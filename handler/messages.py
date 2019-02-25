from flask import jsonify
from dao.messages import MessagesDAO


class MessageHandler:


    def builMessageDict(self, row):
        result = {}
        result['messageId'] = row[0]
        result['content'] = row[1]
        result['messageDate'] = row[2]
        result['messageType'] = row[3]
        return result

    def buildPostAttributes(self, messageId, content, messageDate, messageType):
        result = {}
        result['messageId'] = messageId
        result['content'] = content
        result['messageDate'] = messageDate
        result['messageType'] = messageType
        return result

#---------------Operations---------------------------------------------------------

    def getAllMessages(self):
        dao = MessagesDAO()
        messages_List = dao.getAllMessages()
        return jsonify(messages_List)

    def getMessageById(self, messageId):
        dao = MessagesDAO()
        messages_List = dao.getMessageById(messageId)
        return jsonify(messages_List)

    def getMessagesByChatId(self, chatId):
        dao = MessagesDAO()
        messages_List = dao.getMessagesByChatId(chatId)
        return jsonify(messages_List)

    def getNumOfRepliesByDate(self, date):
        dao = MessagesDAO()
        numOfReplies = dao.getNumOfRepliesByDate(date)
        return jsonify(numOfReplies)

    def getNumOfRepliesByDateAndPost(self, date, postId):
        dao = MessagesDAO()
        numOfReplies = dao.getNumOfRepliesByDateAndUser(date, postId)
        return jsonify(numOfReplies)

    def insertMessage(self, json):
        dao = MessagesDAO()
        newMessage = dao.insertMessage(json)
        return jsonify(newMessage)

    def updateMessage(self, messageId, form):
        dao = MessagesDAO()
        updateMessage = dao.updateMessage(messageId, form)
        return jsonify(updateMessage)

    def deleteMessage(self, messageId):
        dao = MessagesDAO()
        id = dao.deleteMessage(messageId)
        return jsonify(DeleteStatus="OK"), 200

