from config.dbconfig import pg_config
import psycopg2
import datetime
from config.dbconfig import pg_config
import psycopg2

class ReactionsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'],
                                                                           pg_config['host']
                                                                           )

        self.conn = psycopg2._connect(connection_url)

    reactionArray = [{"reactionId": 1, "type": 'like', "date": datetime.datetime.now()},
                 {"reactionId": 2, "type": 'dislike', "date": datetime.datetime.now()},
                 {"reactionId": 3, "type": 'like', "date": datetime.datetime.now()},
                 {"reactionId": 4, "type": 'dislike', "date": datetime.datetime.now()},
                 {"reactionId": 5, "type": 'like', "date": datetime.datetime.now()}]

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select reactionId, postId, userId, messageId, type from Reaction;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getReactionById(self, reactionId):
        cursor = self.conn.cursor()
        query = "select reactionId, postId, userId, messageId, type from Reaction where reactionId=%s;"
        cursor.execute(query, (reactionId,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getReactionsByPostId(self, postId):
        cursor = self.conn.cursor()
        query = "select reactionId, postId, userId, messageId, type from Reaction where postId=%s;"
        cursor.execute(query, (postId,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getReactionsByMessageId(self, messageId):
        cursor = self.conn.cursor()
        query = "select reactionId, postId, userId, messageId, type from Reaction where messageId=%s;"
        cursor.execute(query, (messageId,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getLikesCountByMessageId(self, messageId):
        cursor = self.conn.cursor()
        query = "select messageId, count(reactionId) from Reaction where messageId=%s and type='LIKE' group by messageId;"
        cursor.execute(query, (messageId,))
        result = cursor.fetchone()
        print(result)
        if result is None:
            result=(messageId, 0)
        return result

    def getDislikesCountByMessageId(self, messageId):
        cursor = self.conn.cursor()
        query = "select messageId, count(reactionId) from Reaction where messageId=%s and type='DISLIKE' group by messageId;"
        cursor.execute(query, (messageId,))
        result = cursor.fetchone()
        print(result)
        if result is None:
            result=(messageId, 0)
        return result

    def getUsersWhoLikesByMessageId(self, messageId):
        cursor = self.conn.cursor()
        query = "select userid, username, firstname, lastname, reactiondate from reaction natural inner join users natural inner join person " \
                "where messageid=%s and type='LIKE';"
        cursor.execute(query, (messageId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersWhoDislikesByMessageId(self, messageId):
        cursor = self.conn.cursor()
        query = "select userid, username, firstname, lastname, reactiondate from reaction natural inner join users natural inner join person " \
                "where messageid=%s and type='DISLIKE';"
        cursor.execute(query,(messageId,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReactionById(self, cid):
        cursor = self.conn.cursor()
        query = "select * from chat where chatId = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result


    def reactionsPerMessage(self):
        cursor = self.conn.cursor()
        query = "select likes.messageid, likes.likecount, dislikes.dislikecount from " \
                "(select messageid, count(r.type) as likecount from reaction as r where type = 'LIKE' group by messageid) as likes " \
                "full outer join " \
                "(select messageid, count(r.type) as dislikecount from reaction as r where type = 'DISLIKE' group by messageid) as dislikes " \
                "on likes.messageId = dislikes.messageId order by messageid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReactionsByArgs(self, args):
        return [self.reactionArray[1], self.reactionArray[2]]

    def getLikesCountOnDate(self, date):
        return 541

    def getDislikesCountOnDate(self, date):
        return 149

    def getLikesOfPost(self, postid):
        return 15

    def getDislikesOfPost(self, postid):
        return 9

    def insert(self, userId, postId, messageId, type, reactionDate):
        cursor = self.conn.cursor()
        query = "insert into reaction (userId, postId, messageId, type, reactionDate) values (%s, %s, %s, %s, %s) returning reactionId"
        cursor.execute(query, (userId, postId, messageId, type, reactionDate))
        reactionId = cursor.fetchone()[0]
        self.conn.commit()
        return messageId

    def update(self, pid, form):
        return self.reactionArray[4]

    def delete(self, pid):
        return pid


