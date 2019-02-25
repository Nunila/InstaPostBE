from flask import jsonify
from dao.hashtag import HashtagsDAO


class HashtagHandler:

    def getAllHashtags(self):
        dao = HashtagsDAO()
        hashtags_list = dao.getAllHashtags()
        return jsonify(hashtags_list), 200

    def searchHashtags(self, args):
        dao = HashtagsDAO()
        hashtags_list = dao.getHashByArgs(args)
        return jsonify(hashtags_list), 200

    def getHashtagById(self, hid):
        dao = HashtagsDAO()
        hashtag = dao.getHashById(hid)
        return jsonify(hashtag), 200

    def getTrendingHash(self):
        dao = HashtagsDAO()
        hash = dao.getTrending()
        return jsonify(Hashtag=hash), 200

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

