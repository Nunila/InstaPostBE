from config.dbconfig import pg_config
import psycopg2


class MessagesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'],
                                                                           pg_config['host']
                                                                           )

        self.conn = psycopg2._connect(connection_url)
    
    messagesArray=[{"messageId": 1, "content": 'Insert inspiring caption here', "messageDate": '2/21/2019 12:00:00', "messageType": 'caption'},
                   {"messageId": 2, "content": 'I love your photo!', "messageDate": '2/21/2019 14:00:00', "messageType": 'reply'}]

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select messageId, userId, content, messageDate from message;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, messageId):
        cursor = self.conn.cursor()
        query = "select messageId, userId, content, messageDate from message where messageId = %s;"
        cursor.execute(query, (messageId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByPostId(self, postId):
        cursor = self.conn.cursor()
        query = "select messageId, userId, content, messageDate from message where postId = %s;"
        cursor.execute(query, (postId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByUserId(self, userId):
        cursor = self.conn.cursor()
        query = "select messageId, userId, content, messageDate from message where userId = %s;"
        cursor.execute(query, (userId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReplies(self):
        cursor = self.conn.cursor()
        query = "select messageid, postId, userid, content, messagedate, username from reply natural inner join message natural inner join users;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesByPostId(self, postId):
        cursor = self.conn.cursor()
        query = "select messageid, postId, userid, content, messagedate, username from reply natural inner join message natural inner join users where postId=%s;"
        cursor.execute(query, (postId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByDate(self, messageDate):
        cursor = self.conn.cursor()
        query = "select messageId, userId, content, messageDate, type from message where messageDate = %s;"
        cursor.execute(query, (messageDate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByChatId(self, chatId):
        cursor = self.conn.cursor()
        query = "(select messageId, message.userId, content, messageDate from message " \
                "natural join caption " \
                "inner join post on caption.postId = post.postId " \
                "where chatId=%s) " \
                "union " \
                "(select messageId, message.userId, content, messageDate from message " \
                "natural join reply " \
                "inner join post on reply.postId = post.postId " \
                "where chatId=%s);"
        cursor.execute(query, (chatId, chatId))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumRepliesPerDay(self):
        cursor = self.conn.cursor()
        query = "select date(messageDate), count(*) as repliesPerDay " \
                "                from reply natural inner join message" \
                "                group by messageDate;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumOfRepliesByDate(self, date):
        return 100

    def getNumOfRepliesByDateAndPost(self, date, postId):
        return 20

    def insertMessage(self, userId, content, messageDate):
        cursor = self.conn.cursor()
        query = "insert into message (userId, content, messageDate) values ( %s, %s, %s) returning messageId;"
        cursor.execute(query, (userId, content, messageDate));
        messageId = cursor.fetchone()[0]
        self.conn.commit()
        return messageId

    def updateMessage(self, mid, form):
        return self.messagesArray

    def deleteMessage(self, json):
        return 'Sucessfully deleted!'

    def insertReply(self, postId, messageId):
        cursor = self.conn.cursor()
        query = "insert into reply (postId, messageId) values (%s, %s);"
        cursor.execute(query, (postId, messageId))
        self.conn.commit()
        return "Successfully inserted reply"