import datetime
from config.dbconfig import pg_config
import psycopg2


class HashtagsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            )

        self.conn = psycopg2._connect(connection_url)

    hashtagArray = [{"hashtagId": 1, "hashName": '#TeamRubio', "date": datetime.datetime.now()},
                    {"hashtagId": 2, "hashName": '#GoTS8', "date": datetime.datetime.now()},
                    {"hashtagId": 3, "hashName": '#tbt', "date": datetime.datetime.now()},
                    {"hashtagId": 4, "hashName": '#takemeback', "date": datetime.datetime.now()},
                    {"hashtagId": 5, "hashName": '#blessed', "date": datetime.datetime.now()}]


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
        query = "select * from Hashtag where hashname = %s;"
        cursor.execute(query, (hname,))
        result = cursor.fetchone()
        return result

    def getTrending(self):
        cursor = self.conn.cursor()
        query = "select hashname, count(*) as countPerDay " \
                "from hashtag " \
                "WHERE date(datetime) = date(Now()) " \
                "group by hashname " \
                "order by count(*) desc;"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def insert(self, hname):
        cursor = self.conn.cursor()
        query = "insert into Hashtag(hashName, date) values (%s, %s) returning hashtagId;"
        cursor.execute(query, (hname, datetime.datetime.now(),))
        result = []
        for row in cursor:
            result.append(row)
        return result

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