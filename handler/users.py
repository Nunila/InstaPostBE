from flask import jsonify
from dao import usersDAO

class UsersHandler:

    def getAllUsers(self):
        dao = usersDAO()
        user_list = dao.getAllUsers()
        return jsonify(user_list)

    def getUserByID(self, uid):
        dao = usersDAO()
        user = dao.getUserByID(uid)
        return jsonify(user)

    def getUserByUName(self, uname):
        dao = usersDAO()
        user_list = dao.getUserByUName(uname)
        return jsonify(user_list)

    def insertUserJson(self, json):
        dao = usersDAO()
        new_user = dao.insert(json)
        return jsonify(new_user)

    def updateUser(self, uid, form):
        dao = usersDAO()
        updated_user = dao.update(uid, form)
        return jsonify(updated_user)

    def deleteUser(self, uid):
        dao = usersDAO()
        id = dao.delete(uid)
        return jsonify(DeleteStatus = "OK"), 200

