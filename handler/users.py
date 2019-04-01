from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:

    def buildUserAttributes(self, row):
        result = {}
        result['userId'] = row[0]
        result['userName'] = row[1]
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        return jsonify(user_list), 200

    def getUserByID(self, uid):
        dao = UsersDAO()
        user = dao.getUserByID(uid)
        return jsonify(user), 200

    def getUserByUName(self, uname):
        dao = UsersDAO()
        user_list = dao.getUserByUName(uname)
        return jsonify(user_list), 200

    def getMostActiveUser(self):
        dao = UsersDAO()
        most_active = dao.getMostActiveUser()
        return jsonify(most_active), 200

    def insertUser(self, json):
        dao = UsersDAO()
        new_user = dao.insert(json)
        return jsonify(new_user), 200

    def updateUser(self, uid, form):
        dao = UsersDAO()
        updated_user = dao.update(uid, form)
        return jsonify(updated_user), 200

    def deleteUser(self, uid):
        dao = UsersDAO()
        id = dao.delete(uid)
        return jsonify(DeleteStatus="OK"), 200

