from flask import jsonify
import datetime


class ParticipatesDAO:

    def getAllParticipates(self):
        cursor = self.conn.cursor()
        query = "select participationId, userId, chatId, role from Participates;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getParticipatesByUserId(self, userId):
        cursor = self.conn.cursor()
        query = "select participationId, userId, chatId, role from Participates where userId=%s;"
        cursor.execute(query, (userId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getParticipatesByChatId(self, chatId):
        cursor = self.conn.cursor()
        query = "select participationId, userId, chatId, role from Participates where chatId=%s;"
        cursor.execute(query, (chatId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersOfChatGroup(self, chatId):
        cursor = self.conn.cursor()
        query = "select username, role from Participates" \
                "natural join Users where chatId=%s;"
        cursor.execute(query, (chatId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersSubscribed(self):
        cursor = self.conn.cursor()
        query = "select username, role from Participates" \
                "natural join Users;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result