import datetime


class HashtagsDAO:

    hashtagArray = [{"hashtagId": 1, "hashName": '#TeamRubio', "date": datetime.datetime.now()},
                    {"hashtagId": 2, "hashName": '#GoTS8', "date": datetime.datetime.now()},
                    {"hashtagId": 3, "hashName": '#tbt', "date": datetime.datetime.now()},
                    {"hashtagId": 4, "hashName": '#takemeback', "date": datetime.datetime.now()},
                    {"hashtagId": 5, "hashName": '#blessed', "date": datetime.datetime.now()}]

    def getAllHashtags(self):
        return self.hashtagArray

    def getHashById(self, pid):
        return self.hashtagArray[0]

    def getHashByArgs(self, args):
        return [self.hashtagArray[1], self.hashtagArray[2]]

    def getTrending(self):
        return self.hashtagArray[0]['hashName']

    def insert(self, json):
        return self.hashtagArray[2]

    def update(self, pid, form):
        return self.hashtagArray[4]

    def delete(self, pid):
        return pid