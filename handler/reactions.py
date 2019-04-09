from flask import jsonify
from dao.reactions import ReactionsDAO
from collections import defaultdict


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

    def buildReactionAttribute(self, row):
        result = []
        result['reactionId'] = row[0]
        result['userId'] = row[1]
        result['postId'] = row[2]
        result['messageId'] = row[3]
        result['type'] = row[4]
        return result

    def getAllReactions(self):
        dao = ReactionsDAO()
        reaction_list = dao.getAllReactions()
        results = []
        for row in reaction_list:
            element = self.buildReactionAttributes(row)
            results.append(element)
        return jsonify(Reaction=results), 200

    def getAllReactionsForMessages(self):
        dao = ReactionsDAO()
        reaction_list = dao.reactionsPerMessage()
        # results = self.buildReactionDictionary(reaction_list)
        # return jsonify(results), 200
        results = []
        for row in reaction_list:
            element = self.buildReactionDictionary(row)
            results.append(element)
        return jsonify(results), 200

    def getReactionById(self, cid):
        dao = ReactionsDAO()
        reaction = dao.getReactionById(cid)
        return jsonify(reaction), 200

    def searchReactions(self, args):
        dao = ReactionsDAO()
        reaction_list = dao.getReactionsByArgs(args)
        return jsonify(reaction_list), 200

    def insertReactionJson(self, json):
        dao = ReactionsDAO()
        newreaction = dao.insert(json)
        return jsonify(newreaction), 200

    def updateReaction(self, cid, form):
        dao = ReactionsDAO()
        updatedreaction = dao.update(cid, form)
        return jsonify(updatedreaction), 200

    def deleteReaction(self, cid):
        dao = ReactionsDAO()
        id = dao.delete(cid)
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
