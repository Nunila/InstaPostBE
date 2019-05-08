from flask import jsonify
from dao.messages import MessagesDAO
from handler.hashtag import HashtagHandler
import datetime


class MessageHandler:


    def builMessageDict(self, row):
        result = {}
        result['messageId'] = row[0]
        result['userId'] = row[1]
        result['content'] = row[2]
        result['messageDate'] = row[3]
        return result

    def buildRepliesDict(self, row):
        result = {}
        result['messageId'] = row[0]
        result['postId'] = row[1]
        result['userId'] = row[2]
        result['content'] = row[3]
        result['messageDate'] = row[4]
        result['username'] = row[5]
        return result


    def buildReplyAttributes(self, messageId, postId, userId, content, messageDate):
        result = {}
        result['messageId'] = messageId
        result['postId'] = postId
        result['userId'] = userId
        result['content'] = content
        result['messageDate'] = messageDate
        return result

    def buildMessageAttributes(self, messageId, userId, content, messageDate):
        result = {}
        result['messageId'] = messageId
        result['userId'] = userId
        result['content'] = content
        result['messageDate'] = messageDate
        return result

#---------------Operations---------------------------------------------------------

    def getAllMessages(self):
        dao = MessagesDAO()
        messages_List = dao.getAllMessages()
        result_list = []
        for row in messages_List:
            result = self.builMessageDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getMessageById(self, messageId):
        dao = MessagesDAO()
        messages_List = dao.getMessageById(messageId)
        result_list = []
        for row in messages_List:
            result = self.builMessageDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getMessagesByPostId(self, postId):
        dao = MessagesDAO()
        messages_List = dao.getMessagesByPostId(postId)
        result_list = []
        for row in messages_List:
            result = self.builMessageDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getMessagesByUserId(self, userId):
        dao = MessagesDAO()
        messages_List = dao.getMessagesByUserId(userId)
        result_list = []
        for row in messages_List:
            result = self.builMessageDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getMessagesByDate(self, messageDate):
        dao = MessagesDAO()
        messages_List = dao.getMessagesByDate(messageDate)
        result_list = []
        for row in messages_List:
            result = self.builMessageDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getMessagesByChatId(self, chatId):
        dao = MessagesDAO()
        messages_List = dao.getMessagesByChatId(chatId)
        result_list = []
        for row in messages_List:
            result = self.builMessageDict(row)
            result_list.append(result)

        return jsonify(result_list)

#----------------------------Replies--------------------------------------------------

    def getAllReplies(self):
        dao = MessagesDAO()
        messages_List = dao.getAllReplies()
        result_list = []
        for row in messages_List:
            result = self.buildRepliesDict(row)
            result_list.append(result)
            print(row)
        return jsonify(result_list)

    def getRepliesByPostId(self, postId):
        dao = MessagesDAO()
        messages_List = dao.getRepliesByPostId(postId)
        result_list = []
        for row in messages_List:
            result = self.buildRepliesDict(row)
            result_list.append(result)

        return jsonify(result_list)


    def getNumOfRepliesByDate(self, date):
        dao = MessagesDAO()
        numOfReplies = dao.getNumOfRepliesByDate(date)
        return jsonify(numOfReplies)

    def getNumOfRepliesByDateAndPost(self, date, postId):
        dao = MessagesDAO()
        numOfReplies = dao.getNumOfRepliesByDateAndPost(date, postId)
        return jsonify(numOfReplies)

    def insertMessage(self, json):
        userId = json['userId']
        content = json['content']
        messageDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if userId and content and messageDate:
            dao = MessagesDAO()
            messageId = dao.insertMessage(userId, content, messageDate)
            result = self.buildMessageAttributes(messageId, userId, content, messageDate)

            hashHandler = HashtagHandler()
            hashResult = hashHandler.getHashtagsFromString(content)
            if(hashResult) is not None:
                hashHandler.insertHashtagArray(hashResult, messageId)
            #print("Result: ", jsonify(result))
            return messageId, 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateMessage(self, messageId, form):
        dao = MessagesDAO()
        updateMessage = dao.updateMessage(messageId, form)
        return jsonify(updateMessage)

    def deleteMessage(self, messageId):
        dao = MessagesDAO()
        id = dao.deleteMessage(messageId)
        return jsonify(DeleteStatus="OK"), 200

    def insertReplyJson(self, json):
        postId = json['postId']
        userId = json['userId']
        content = json['content']
        messageDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if postId and userId and content and messageDate:
            dao = MessagesDAO()
            messageId = dao.insertMessage(userId, content, messageDate)
            result = self.buildReplyAttributes(messageId, postId, userId, content, messageDate)
            notification = dao.insertReply(postId, messageId)
            print(notification)

            hashHandler = HashtagHandler()
            hashresult = hashHandler.getHashtagsFromString(content)
            if hashresult is not None:
                hashHandler.insertHashtagArray(hashresult, messageId)

            return jsonify(result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


