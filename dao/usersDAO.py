from config import dbconfig
import psycopg2

class UsersDAO:

    userArray = [{"userId": 1, "userName": 'Homero123', "password": 'dotdashdot'},
                 {"userId": 2, "userName": 'Salchicha2', "password": 'bootwoot9'}]

 #   def _init_(self):

  #      connectionURL=""

   #     self.conn = psycopg2._connect(connectionURL)

    def getAllUsers(self):
        return self.userArray

    def getUserByID(self, uid):
        return self.userArray[0]

    def getUserByUName(self, uname):
        return self.userArray[1]

    def insert(self, json):
        return self.userArray[1]

    def update(self, uid, form):
        return self.userArray[1]

    def delete(self, uid):
        return uid

