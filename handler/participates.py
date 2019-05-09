from flask import jsonify
from dao.participates import ParticipatesDAO


class ParticipatesHandler:

    def buildUserDict(self, row):
        result = {}
        result['firstName'] = row[0]
        result['lastName'] = row[1]
        result['phonenumber'] = row[2]
        result['email'] = row[3]
        result['birthday'] = row[4]
        result['userName'] = row[5]
        result['userId'] = row[6]
        result['personId'] = row[7]
        return result

    def buildParticipatesDict(self, row):
        result = {}
        result['personId'] = row[0]
        result['userId'] = row[1]
        result['username'] = row[2]
        result['firstname'] = row[3]
        result['lastname'] = row[4]
        result['phonenumber'] = row[5]
        result['email'] = row[6]
        result['birthday'] = row[7]
        return result

    def buildParticipatesDict2(self, userId, chatId, role):
        result = {}
        result['userId'] = userId
        result['chatId'] = chatId
        result['role'] = role
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
        if not user_List:
            return jsonify(Error="Chat Not Found"), 404
        else:
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

    def getContactsNotInChat(self, personId, chatId):
        dao = ParticipatesDAO()
        contacts_list = dao.getContactsNotInChat(personId, chatId)
        result_list = []
        for row in contacts_list:
            result = self.buildParticipatesDict(row)
            result_list.append(result)
        return jsonify(result_list)

    def insertNewChatJson(self, chatId, json):
        owner = json['ownerId']
        members = json['members']

        if owner and members and chatId:
            dao = ParticipatesDAO()
            dao.insert(chatId, owner, 'owner')
            for member in members:
                dao.insert(chatId, member, 'member')

                # result = self.build_chat_attributes(chatid, chatname, creationDate)
            return jsonify(json), 201
        else:

            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertParticipantsToChat(self, json, chatId):
        participants = json['participants']
        role = "member"
        if chatId and participants:
            dao = ParticipatesDAO()
            result = []
            for user in participants:
                userId = dao.insert(chatId, user, role)
                result.append(self.buildParticipatesDict2(user, chatId, role))
            return jsonify(result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
