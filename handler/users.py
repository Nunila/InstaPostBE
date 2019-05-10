from flask import jsonify
from dao.users import UsersDAO
from dao.person import PersonDAO
from collections import OrderedDict


class UsersHandler:


    def buildMostActiveUsersDict(self, row):
        result = {}
        result['userId'] = row[0]
        result['day'] = row[1]
        result['count'] = row[2]
        result['username'] = row[3]
        return result

#userId, username, personId, firstName, lastName, phoneNumber, email, birthday
    def buildUserAttributes(self, row):
        result = {}
        result['userId'] = row[0]
        result['username'] = row[1]
        result['personId'] = row[2]
        result['firstName'] = row[3]
        result['lastName'] = row[4]
        result['phoneNum'] = row[5]
        result['email'] = row[6]
        result['birthday'] = row[7]
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



    def getMostActiveUsersByDate(self):
        dao = UsersDAO()
        most_active = dao.getMostActiveUsersByDate()
        results = []
        map = {}
        for row in most_active:
            element = self.buildMostActiveUsersDict(row)
            results.append(element)
            map[str(element['day'])] = []
        for row in results:
            map[str(row['day'])].append(row)

        return jsonify(map), 200



# MADE FOR LOG IN PURPOSES#
    def userLogin(self, username, password):
        dao = UsersDAO()
        result = dao.getUserLogin(username, password)
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

