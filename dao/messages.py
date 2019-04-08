from config.dbconfig import pg_config
import psycopg2


class MessagesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            )

        self.conn = psycopg2._connect(connection_url)
    
    messagesArray=[{"messageId": 1, "content": 'Insert inspiring caption here', "messageDate": '2/21/2019 12:00:00', "messageType": 'caption'},
                   {"messageId": 2, "content": 'I love your photo!', "messageDate": '2/21/2019 14:00:00', "messageType": 'reply'}]

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select messageId, postId, userId, content, messageDate, type from message;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, messageId):
        cursor = self.conn.cursor()
        query = "select messageId, postId, userId, content, messageDate, type from message where messageId = %s;"
        cursor.execute(query, (messageId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByPostId(self, postId):
        cursor = self.conn.cursor()
        query = "select messageId, postId, userId, content, messageDate, type from message where postId = %s;"
        cursor.execute(query, (postId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByUserId(self, userId):
        cursor = self.conn.cursor()
        query = "select messageId, postId, userId, content, messageDate, type from message where userId = %s;"
        cursor.execute(query, (userId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReplies(self):
        cursor = self.conn.cursor()
        query = "select messageid, postid, userid, content, messagedate from reply natural inner join message;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesByPostId(self, postId):
        cursor = self.conn.cursor()
        query = "select messageid, postid, userid, content, messagedate from reply natural inner join message where postId=%s;"
        cursor.execute(query, (postId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByDate(self, messageDate):
        cursor = self.conn.cursor()
        query = "select messageId, postId, userId, content, messageDate, type from message where messageDate = %s;"
        cursor.execute(query, (messageDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByChatId(self, chatId):
        cursor = self.conn.cursor()
        query = "(select messageId, post.postId, message.userId, content, messageDate, type from message " \
                "natural join caption " \
                "inner join post on caption.postId = post.postId " \
                "where chatId=%s) " \
                "union " \
                "(select messageId, post.postId, message.userId, content, messageDate, type from message " \
                "natural join reply " \
                "inner join post on reply.postId = post.postId " \
                "where chatId=%s);"
        cursor.execute(query, (chatId, chatId))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumOfRepliesByDate(self, date):
        return 100

    def getNumOfRepliesByDateAndPost(self, date, postId):
        return 20

    def insertMessage(self,json):
        return 'Succesfully inserted new message!'

    def updateMessage(self, mid, form):
        return self.messagesArray

    def deleteMessage(self, json):
        return 'Sucessfully deleted!'