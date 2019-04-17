from config.dbconfig import pg_config
import psycopg2
import os

class PostsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'],
                                                                           pg_config['host'],
                                                                           pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    postsArray = [{"postId": 1, "photoId": '345C6', "postDate": '2/21/2019 12:00:00'},
                  {"postId": 2, "photoId": '265A2', "postDate": '2/14/2018 15:00:00'},
                  {"postId": 3, "photoId": '542B1', "postDate": '2/17/2019 21:00:00'},
                  {"postId": 4, "photoId": '21476', "postDate": '2/23/2019 11:00:00'},
                  {"postId": 5, "photoId": '635W9', "postDate": '5/01/2019 4:00:00'}]

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select postid, userid, messageid, chatid, photourl, postdate, content, username " \
                "from post natural inner join message natural inner join users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getPostById(self, postId):
        cursor = self.conn.cursor()
        query = "select postId, chatId, userId, photourl, messageId, content, postDate " \
                "from post natural inner join message where postId = %s;"
        cursor.execute(query, (postId,))
        result = cursor.fetchone()

        return result

    def getPostsByUserId(self, userId):
        cursor = self.conn.cursor()
        query = "select postId, chatId, userId, photourl, messageId, content, postDate " \
                "from post natural inner join message where userId = %s;"
        cursor.execute(query, (userId,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getPostsByChatId(self, chatId):
        cursor = self.conn.cursor()
        query = "select postId, chatId, userId, photourl, messageId, content, postDate " \
                "from post natural inner join message where chatId = %s;"
        cursor.execute(query, (chatId,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getPostsByDate(self, postDate):
        cursor = self.conn.cursor()
        query = "select postId, chatId, userId, photourl, messageId, content, postDate " \
                "from post natural inner join message where postDate = %s;"
        cursor.execute(query, (postDate,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getNumberOfPostsPerDay(self):
        cursor = self.conn.cursor()
        query = "select date(postdate), count(*) as postsPerDay " \
                "from post " \
                "group by postdate;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getNumOfPostsByDateAndUser(self, date, userId):
        return 8

    def getNumOfPostsByDate(self, date):
        return 100

    def insertPost(self, json):
        return 'Succesfully inserted new post!'

    def updatePost(self, pid, form):
        return self.postsArray[2]

    def deletePost(self, json):
        return 'Sucessfully deleted!'


