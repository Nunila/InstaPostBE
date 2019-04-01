from flask import jsonify
from dao.participates import ParticipatesDAO


class ParticipatesHandler:

    def buildUserDict(self, row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['phonenumber'] = row[2]
        result['email'] = row[3]
        result['birthday'] = row[4]
        result['username'] = row[5]
        return result

    def buildParticipatesAttributes(self, postId, chatId, userId, photourl, postDate):
        result = {}
        result['postId'] = postId
        result['chatId'] = chatId
        result['userId'] = userId
        result['photourl'] = photourl
        result['postDate'] = postDate
        return result

#---------------Operations---------------------------------------------------------

    def getUsersInSpecificChat(self, chatid):
        dao = ParticipatesDAO()
        user_List = dao.getUsersInSpecificChat(chatid)
        result_list = []
        for row in user_List:
            result = self.buildUserDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getOwnerInSpecificChat(self, chatid):
        dao = ParticipatesDAO()
        row = dao.getOwnerInSpecificChat(chatid)
        if not row:
            return jsonify(Error="Chat Not Found"), 404
        else:
            user = self.buildUserDict(row)

        return jsonify(User=user)