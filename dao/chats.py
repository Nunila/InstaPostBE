
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
        query = "select chatid, chatname, creationdate, userid from chat natural inner join participates " \
                "where role='owner';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatById(self, cid):
        cursor = self.conn.cursor()
        query = "select * from chat where chatId = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getChatsByParticipatingId(self, uid):
        cursor = self.conn.cursor()
        query = "select chatid, chatname, creationdate, userid from chat natural inner join participates " \
                "where userid= %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatsByArgs(self, args):
        return [self.chatArray[1], self.chatArray[2]]

    def getChatsByMemberId(self, uid):
        return [self.chatArray[3], self.chatArray[4]]

    def insert(self, chatname, creationdate):
        cursor = self.conn.cursor()
        query = "insert into chat(chatName, creationDate) values (%s, %s) returning chatid;"
        cursor.execute(query, (chatname, creationdate,))
        pid = cursor.fetchone()[0]
        self.conn.commit()

        return pid

    def addContactToChat(self, cid, pid):
        return "Contact added successfully to chat."

    def update(self, pid, form):
        return self.chatArray[4]

    def delete(self, pid):
        return pid

    def deleteContactFromChat(self, cid, personid):
        return





