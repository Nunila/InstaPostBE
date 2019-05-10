from flask import jsonify
from dao.users import UsersDAO
from dao.person import PersonDAO

class UsersHandler:


#userId, username, personId, firstName, lastName, phoneNumber, email, birthday
    def buildUserAttributes(self, row):
        result = {}
        result['userId'] = row[0]
        result['userName'] = row[1]
        result['personId'] = row[3]
        result['firstName'] = row[4]
        result['lastName'] = row[5]
        result['phoneNum'] = row[6]
        result['email'] = row[7]
        result['birthday'] = row[8]
        return result
#*
# MADE FOR LOG IN PURPOSES#
    def buildLoginCredentials(self, row):
        result = {}
        result['userId'] = row[0]
        result['userName'] = row[1]
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        results = []
        for row in user_list:
            element = self.buildUserAttributes(row)
            results.append(element)
        return jsonify(Users= results), 200

    def getUserByID(self, uid):
        dao = UsersDAO()
        result = dao.getUserByID(uid)
        if not result:
            return jsonify(Error = 'User not found.'), 404
        else:
            user = self.buildUserAttributes(result)
            return jsonify(User= user), 200

    def getUserByUName(self, uname):
        dao = UsersDAO()
        result = dao.getUserByUName(uname)
        if not result:
            return jsonify(Error='User not found.'), 404
        else:
            user = self.buildUserAttributes(result)
            return jsonify(User= user), 200

    def getMostActiveUser(self):
        dao = UsersDAO()
        most_active = dao.getMostActiveUser()
        return jsonify(most_active), 200
#*
# MADE FOR LOG IN PURPOSES#
    def userLogin(self, json):
        print('this is the json', json)
        dao = UsersDAO()
        result = dao.getUserLogin(json)
        print(result)
        if not result:
            return jsonify(Error='Invalid Credentials.'), 405
        else:
            user = self.buildUserAttributes(result)
            return jsonify(User= user), 200

    def insertUser(self, json):
        dao = UsersDAO()
        new_user = dao.insert(json)
        if not new_user:
            return jsonify(ERROR="This username is taken."), 400
        else:
            result = dao.getUserByID(new_user)
            user = self.buildUserAttributes(result)
            return jsonify(User= user)

    def updateUser(self, uid, form):
        dao = UsersDAO()
        updated_user = dao.update(uid, form)
        return jsonify(updated_user), 200

    def deleteUser(self, uid):
        dao = UsersDAO()
        id = dao.delete(uid)
        return jsonify(DeleteStatus="OK"), 200

