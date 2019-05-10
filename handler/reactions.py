from flask import jsonify
from dao.reactions import ReactionsDAO
from collections import defaultdict
import datetime


class ReactionHandler:

    def buildReactionDictionary(self, row):
        result = {}
        result['messageId'] = row[0]
        result['likes'] = row[1]
        result['dislikes'] = row[2]
        if result['likes'] is None:
            result['likes'] = 0
        if result['dislikes'] is None:
            result['dislikes'] = 0
        return result

    def buildUserReactionDictionary(self, row):
        result = {}
        result['userId'] = row[0]
        result['userName'] = row[1]
        result['firstName'] = row[2]
        result['lastName'] = row[3]
        result['reactiondate'] = row[4]
        return result

    def buildReactionAttribute(self, row):
        result = []
        result['reactionId'] = row[0]
        result['userId'] = row[1]
        result['postId'] = row[2]
        result['messageId'] = row[3]
        result['type'] = row[4]
        return result

    def buildLikesCountDictionary(self, row):
        result ={}
        result['messageId']=row[0]
        result['likesCount']=row[1]
        return result

    def buildDislikesCountDictionary(self, row):
        result ={}
        result['messageId']=row[0]
        result['dislikesCount']=row[1]
        return result

    def buildReactionAttributes(self, reactionId, userId, postId, messageId, type, reactionDate):
        result = {}
        result['reactionId'] = reactionId
        result['userId'] = userId
        result['postId'] = postId
        result['messageId'] = messageId
        result['type'] = type
        result['reactionDate'] = reactionDate
        return result

    def buildUserReactionDict2(self, row):
        result = {}
        result['reactionId'] = row[0]
        result['userId'] = row[1]
        result['postId'] = row[2]
        result['messageId'] = row[3]
        result['type'] = row[4]
        result['reactionDate'] = row[5]
        return result

#--------------Operations-----------------------------------------------------------------------
    def getAllReactions(self):
        dao = ReactionsDAO()
        reaction_list = dao.getAllReactions()
        results = []
        for row in reaction_list:
            element = self.buildReactionDictionary(row)
            results.append(element)
        return jsonify(results), 200

    def getAllReactionsForMessages(self):
        dao = ReactionsDAO()
        reaction_list = dao.reactionsPerMessage()
        # results = self.buildReactionDictionary(reaction_list)
        # return jsonify(results), 200
        results = []
        for row in reaction_list:
            element = self.buildReactionDictionary(row)
            results.append(element)
        print(results)
        return jsonify(results), 200

    def getLikesCountByMessageId(self, messageId):
        dao = ReactionsDAO()
        count = dao.getLikesCountByMessageId(messageId)
        result = self.buildLikesCountDictionary(count)
        return jsonify(result), 200


    def getDislikesCountByMessageId(self, messageId):
        dao = ReactionsDAO()
        count = dao.getDislikesCountByMessageId(messageId)
        result = self.buildDislikesCountDictionary(count)
        return jsonify(result), 200

    def getReactionById(self, cid):
        dao = ReactionsDAO()
        reaction = dao.getReactionById(cid)
        return jsonify(reaction), 200

    def getUsersWhoLikesByMessageId(self, messageId):
        dao = ReactionsDAO()
        reaction_list = dao.getUsersWhoLikesByMessageId(messageId)
        results = []
        for row in reaction_list:
            result = self.buildUserReactionDictionary(row)
            results.append(result)
        return jsonify(results), 200

    def getUsersWhoDislikesByMessageId(self, messageId):
        dao = ReactionsDAO()
        reaction_list = dao.getUsersWhoDislikesByMessageId(messageId)
        results = []
        for row in reaction_list:
            result = self.buildUserReactionDictionary(row)
            results.append(result)
        return jsonify(results), 200

    def searchReactions(self, args):
        dao = ReactionsDAO()
        reaction_list = dao.getReactionsByArgs(args)
        return jsonify(reaction_list), 200

    def insertReactionJson(self, json):
        userId = json['userId']
        postId = json['postId']
        messageId = json['messageId']
        type = json['reactionType']
        reactionDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if userId and postId and messageId and type and reactionDate:
            dao = ReactionsDAO()
            reactionId = dao.insert(userId, postId, messageId, type, reactionDate)
            newreaction = self.buildReactionAttributes(reactionId, userId, postId, messageId, type, reactionDate)
        return jsonify(newreaction), 200

    def updateReaction(self, cid, form):
        dao = ReactionsDAO()
        updatedreaction = dao.update(cid, form)
        return jsonify(updatedreaction), 200

    def deleteReaction(self, userId, messageId):
        dao = ReactionsDAO()
        id = dao.delete(userId, messageId)
        return jsonify(DeleteStatus="OK"), 200

    def getLikesCountOnDate(self, date):
        dao = ReactionsDAO()
        count = dao.getLikesCountOnDate(date)
        return jsonify(LikesOnDate=count), 200

    def getDislikesCountOnDate(self, date):
        dao = ReactionsDAO()
        count = dao.getDislikesCountOnDate(date)
        return jsonify(DislikesOnDate=count), 200

    def getLikesOfPost(self, postId):
        dao = ReactionsDAO()
        count = dao.getLikesOfPost(postId)
        return jsonify(LikesOnPost=count)

    def getDislikesOfPost(self, postId):
        dao = ReactionsDAO()
        count = dao.getDislikesOfPost(postId)
        return jsonify(DislikesOnPost=count)

    def getUserReactionsByChatId(self, userId, chatId):
        dao = ReactionsDAO()
        reaction_list = dao.getUserReactionsByChatId(userId, chatId)
        results = []
        for row in reaction_list:
            element = self.buildUserReactionDict2(row)
            results.append(element)
        return jsonify(results), 200
