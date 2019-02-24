from flask import jsonify
from dao.usersDAO import UsersDAO

class UsersHandler:

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        return jsonify(user_list)

    def getUserByID(self, uid):
        dao = UsersDAO()
        user = dao.getUserByID(uid)
        return jsonify(user)

    def getUserByUName(self, uname):
        dao = UsersDAO()
        user_list = dao.getUserByUName(uname)
        return jsonify(user_list)

    def insertUserJson(self, json):
        dao = UsersDAO()
        new_user = dao.insert(json)
        return jsonify(new_user)

    def updateUser(self, uid, form):
        dao = UsersDAO()
        updated_user = dao.update(uid, form)
        return jsonify(updated_user)

    def deleteUser(self, uid):
        dao = UsersDAO()
        id = dao.delete(uid)
        return jsonify(DeleteStatus = "OK"), 200

