from flask import jsonify
from los_DAO import usersDAO

class UsersHandler:

    def getAllUsers(self):
        dao = usersDAO()
        user_list = dao.getAllUsers()
        return jsonify(user_list)

