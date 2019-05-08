from flask import jsonify
from dao.hashtag import HashtagsDAO
import datetime

class HashtagHandler:

    def buildHashtagDict(self, row):
        result = {}
        result['hashtagId'] = row[0]
        result['hashName'] = row[1]
        result['date'] = row[2]
        return result

    def buildHashtagForTrending(self, row, index):
        print("row: ", row)
        result = {}
        result['hashtag'] = row[0]
        result['position'] = index
        return result

    def buildHashtagAttributes(self, hashtagId, hashName, datetime):
        result = {}
        result['hashtagId'] = hashtagId
        result['hashName'] = hashName
        result['datetime'] = datetime
        return result

#----------------Operations-----------------

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
        return jsonify(Hashtag=results), 200

    def insertHashtagJson(self, json):
        hashtagsList = json.loads(json)
        for row in hashtagsList:
            hashName = row['hashName']
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            messageId = row['messageId']

            if hashName and timestamp:
                dao = HashtagsDAO()
                searchResult = dao.getHashByName(hashName)
                resultList = []
                if searchResult is None:
                    hashtagId = dao.insert(hashName, timestamp)
                    result = self.buildHashtagAttributes(hashtagId, hashName, timestamp)
                    notification = dao.insertMentioned(hashtagId, messageId)
                    resultList.append(result)
                    print(notification)
                else:
                    resulthashId = searchResult[0]
                    notification = dao.insertMentioned(resulthashId, messageId)
                    result = self.buildHashtagAttributes(resulthashId, hashName, timestamp)
                    resultList.append(result)
                    print(notification)
                return jsonify(resultList), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertHashtagArray(self, list, messageId):
        for hashName in list:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if hashName and timestamp:
                dao = HashtagsDAO()
                searchResult = dao.getHashByName(hashName)
                resultList = []
                if searchResult is None:
                    hashtagId = dao.insert(hashName, timestamp)
                    result = self.buildHashtagAttributes(hashtagId, hashName, timestamp)
                    notification = dao.insertMentioned(hashtagId, messageId)
                    resultList.append(result)
                    print(notification)
                else:
                    resulthashId = searchResult[0]
                    notification = dao.insertMentioned(resulthashId, messageId)
                    result = self.buildHashtagAttributes(resulthashId, hashName, timestamp)
                    resultList.append(result)
                    print(notification)
                return jsonify(resultList), 200
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateHashtag(self,hid, form):
        dao = HashtagsDAO()
        updatedhashtag = dao.update(hid, form)
        return jsonify(updatedhashtag), 200

    def deleteHashtag(self, hid):
        dao = HashtagsDAO()
        result = dao.delete(hid)
        return jsonify(DeleteStatus="OK"), 200

    def getHashtagsFromString(self, content):
        list = []
        if content is not None:
            list = {tag.strip("#") for tag in content.split() if tag.startswith("#")}

        return list


