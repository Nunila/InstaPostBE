import datetime
from config import dbconfig
import psycopg2

class HashtagsDAO:

    hashtagArray = [{"hashtagId": 1, "hashName": '#TeamRubio', "date": datetime.datetime.now()},
                    {"hashtagId": 2, "hashName": '#GoTS8', "date": datetime.datetime.now()},
                    {"hashtagId": 3, "hashName": '#tbt', "date": datetime.datetime.now()},
                    {"hashtagId": 4, "hashName": '#takemeback', "date": datetime.datetime.now()},
                    {"hashtagId": 5, "hashName": '#blessed', "date": datetime.datetime.now()}]

    def _init_(self):
        connectionURL="dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                         dbconfig['user'],
                                                         dbconfig['passwd'])

        self.conn = psycopg2._connect(connectionURL)

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "select * from Hashtag;" 
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashById(self, hid):
        cursor = self.conn.cursor()
        query = "select * from Hashtag where hashtagId = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        return result

    def getHashByName(self, hname):
        cursor = self.conn.cursor()
        query = "select * from Hashtag where hashName = %s;"
        cursor.execute(query, (hname,))
        result = cursor.fetchone()
        return result

    def getTrending(self):
        cursor = self.conn.cursor()
        query = "select * from Hashtag;"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def insert(self, hname):
        cursor = self.conn.cursor()
        query = "insert into Hashtag(hashName, date) values (%s, %s) returning hashtagId;"
        cursor.execute(query, (hname, datetime.datetime.now(),))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def update(self, hid, hname):
        cursor = self.conn.cursor()
        query = "update Hashtag set hname = %s where hashtagId = %s;"
        cursor.execute(query, (hname, hid,))
        self.conn.commit()
        return hid

    def delete(self, hid):
        cursor = self.conn.cursor()
        query = "delete from Hashtag where hashtagId = %s;"
        cursor.execute(query, (hid,))
        self.conn.commit()
        return hid