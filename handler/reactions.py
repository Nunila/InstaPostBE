from flask import jsonify
from dao.reactions import ReactionsDAO


class ReactionHandler:

    def buildReactionDict(self, row):
        result = {}
        result['reactionId'] = row[0]
        result['userId'] = row[1]
        result['postId'] = row[2]
        result['messageId'] = row[3]
        result['type'] = row[4]
        return result

#------------------Operations---------------------------------------------------------------------

    def getAllReactions(self):
        dao = ReactionsDAO()
        reactions_List = dao.getAllReactions()
        result_list = []
        for row in reactions_List:
            result = self.buildReactionDict(row)
            result_list.append(result)

        return jsonify(Message=result_list), 200

    def getReactionById(self, reactionId):
        dao = ReactionsDAO()
        reactions_List = dao.getReactionById(reactionId)
        result_list = []
        for row in reactions_List:
            result = self.buildReactionDict(row)
            result_list.append(result)

        return jsonify(Message=result_list), 200

    def getReactionsByPostId(self, postId):
        dao = ReactionsDAO()
        reactions_List = dao.getReactionsByPostId(postId)
        result_list = []
        for row in reactions_List:
            result = self.buildReactionDict(row)
            result_list.append(result)

        return jsonify(Message=result_list), 200

    def getReactionsByUserId(self, userId):
        dao = ReactionsDAO()
        reactions_List = dao.getReactionsByUserId(userId)
        result_list = []
        for row in reactions_List:
            result = self.buildReactionDict(row)
            result_list.append(result)

        return jsonify(Message=result_list), 200

    def getReactionsByMessageId(self, messageId):
        dao = ReactionsDAO()
        reactions_List = dao.getReactionsByMessageId(messageId)
        result_list = []
        for row in reactions_List:
            result = self.buildReactionDict(row)
            result_list.append(result)

        return jsonify(Message=result_list), 200

    def getLikesCountByMessageId(self, messageId):
        dao = ReactionsDAO()
        count = dao.getLikesCountByMessageId(messageId)
        return jsonify(count), 200

    def getDislikesCountByMessageId(self, messageId):
        dao = ReactionsDAO()
        count = dao.getDislikesCountByMessageId(messageId)
        return jsonify(count), 200


    def getDislikesUsers(self):
        dao = ReactionsDAO()
        reactions_List = dao.getDislikesUsers()
        result_list = []
        for row in reactions_List:
            result_list.append(row)

        return jsonify(Message=result_list), 200

    def getLikesUsers(self):
        dao = ReactionsDAO()
        reactions_List = dao.getLikesUsers()
        result_list = []
        for row in reactions_List:
            result_list.append(row)

        return jsonify(Message=result_list), 200

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








