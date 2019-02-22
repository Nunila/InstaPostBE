from flask import jsonify
from dao.reactions import ReactionsDAO


class ReactionHandler:

    def build_reaction_attributes(self, cid, cname, cowner, date):
        result = {}
        result['reactionId'] = cid
        result['reactionName'] = cname
        result['reactionOwnerId'] = cowner
        result['creationDate'] = date
        return result

#-------------------------Modifications-----------------------------
    def getAllReactions(self):
        dao = ReactionsDAO()
        reactions_list = dao.getAllReactions()
        return jsonify(reactions_list)

    def getReactionById(self, cid):
        dao = ReactionsDAO()
        reaction = dao.getReactionById(cid)
        return jsonify(reaction)

    def searchReactions(self, args):
        dao = ReactionsDAO()
        reaction_list = dao.getReactionsByArgs(args)
        return jsonify(reaction_list)

    def insertReactionJson(self, json):
        dao = ReactionsDAO()
        newreaction = dao.insert(json)
        return jsonify(newreaction)

    def updateReaction(self, cid, form):
        dao = ReactionsDAO()
        updatedreaction = dao.update(cid, form)
        return jsonify(updatedreaction)

    def deleteReaction(self, cid):
        dao = ReactionsDAO()
        id = dao.delete(cid)
        return jsonify(DeleteStatus = "OK"), 200








