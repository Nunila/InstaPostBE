
import datetime
from config.dbconfig import pg_config
import psycopg2


class ChatsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            )

        self.conn = psycopg2._connect(connection_url)

    chatArray = [{"chatId": 1, "chatName": 'DBProject', "creationDate": datetime.datetime.now()},
                 {"chatId": 2, "chatName": 'Family', "creationDate": datetime.datetime.now()},
                 {"chatId": 3, "chatName": 'Game of Thrones viewing party', "creationDate": datetime.datetime.now()},
                 {"chatId": 4, "chatName": 'Capstone', "creationDate": datetime.datetime.now()},
                 {"chatId": 5, "chatName": 'BestFriends', "creationDate": datetime.datetime.now()}]

    def getAllChats(self):
        cursor = self.conn.cursor()
        query = "select * from chat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result
        #return self.chatArray

    def getChatById(self, pid):
        return self.chatArray[0]

    def getChatsByArgs(self, args):
        return [self.chatArray[1], self.chatArray[2]]

    def getChatsByMemberId(self, uid):
        return [self.chatArray[3], self.chatArray[4]]

    def insert(self, json):
        return self.chatArray[2]

    def addContactToChat(self, cid, pid):
        return "Contact added successfully to chat."

    def update(self, pid, form):
        return self.chatArray[4]

    def delete(self, pid):
        return pid

    def deleteContactFromChat(self, cid, personid):
        return





