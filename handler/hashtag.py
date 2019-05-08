from flask import jsonify
from dao.hashtag import HashtagsDAO


class HashtagHandler:

    def buildHashtagAttributes(self, row):
        result = {}
        result['hashtagId'] = row[0]
        result['hashName'] = row[1]
        result['date'] = row[2]
        return result

    def buildHashtagForTrending(self, row, index):
        print("row: ", row)
        result = {}
        result['hashtag'] = row[0]
        result['countOnDay'] = row[1]
        result['position'] = index
        return result

    def getAllHashtags(self):
        dao = HashtagsDAO()
        hashtags_list = dao.getAllHashtags()
        results = []
        for row in hashtags_list:
            element = self.buildHashtagAttributes(row)
            results.append(element)
        return jsonify(Hashtag= results), 200

    def searchHashtags(self, hname):
        dao = HashtagsDAO()
        result = dao.getHashByName(hname)
        if not result:
            return jsonify(Error = 'Hashtag not found.'), 404
        else:
            hashtag = self.buildHashtagAttributes(result)
            return jsonify(Hashtag= hashtag), 200

    def getHashtagById(self, hid):
        dao = HashtagsDAO()
        result = dao.getHashById(hid)
        if not result:
            return jsonify(Error = 'Hashtag not found.'), 404
        else:
            hashtag = self.buildHashtagAttributes(result)
            return jsonify(Hashtag= hashtag), 200

    def getTrendingHash(self):
        dao = HashtagsDAO()
        hashtags_list = dao.getTrending()
        results = []
        index = 1
        for row in hashtags_list:
            element = self.buildHashtagForTrending(row, index)
            index += 1
            results.append(element)
        return jsonify(results), 200

    def insertHashtagJson(self, json):
        dao = HashtagsDAO()
        newhashtag = dao.insert(json)
        return jsonify(newhashtag), 200

    def updateHashtag(self,hid, form):
        dao = HashtagsDAO()
        updatedhashtag = dao.update(hid, form)
        return jsonify(updatedhashtag), 200

    def deleteHashtag(self, hid):
        dao = HashtagsDAO()
        result = dao.delete(hid)
        return jsonify(DeleteStatus="OK"), 200

