from config.dbconfig import pg_config
import psycopg2

class PostsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            )

        self.conn = psycopg2._connect(connection_url)

    postsArray = [{"postId": 1, "photoId": '345C6', "postDate": '2/21/2019 12:00:00'},
                  {"postId": 2, "photoId": '265A2', "postDate": '2/14/2018 15:00:00'},
                  {"postId": 3, "photoId": '542B1', "postDate": '2/17/2019 21:00:00'},
                  {"postId": 4, "photoId": '21476', "postDate": '2/23/2019 11:00:00'},
                  {"postId": 5, "photoId": '635W9', "postDate": '5/01/2019 4:00:00'}]

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from post;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getPostById(self, postId):
        return self.postsArray[0]

    def getPostsByUserId(self, userId):
        return self.postsArray[0]

    def getPostsByChatId(self, chatId):
        return self.postsArray

    def getPostsByDate(self, postDate):
        return self.postsArray[4]

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


