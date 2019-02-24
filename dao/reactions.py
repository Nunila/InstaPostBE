
import datetime


class ReactionsDAO:

    reactionArray = [{"reactionId": 1, "type": 'like', "date": datetime.datetime.now()},
                 {"reactionId": 2, "type": 'dislike', "date": datetime.datetime.now()},
                 {"reactionId": 3, "type": 'like', "date": datetime.datetime.now()},
                 {"reactionId": 4, "type": 'dislike', "date": datetime.datetime.now()},
                 {"reactionId": 5, "type": 'like', "date": datetime.datetime.now()}]

    def getAllReactions(self):
        return self.reactionArray

    def getReactionById(self, pid):
        return self.reactionArray[0]

    def getReactionsByArgs(self, args):
        return [self.reactionArray[1], self.reactionArray[2]]

    def insert(self, json):
        return self.reactionArray[2]

    def update(self, pid, form):
        return self.reactionArray[4]

    def delete(self, pid):
        return pid

    def getLikesCountOnDate(self, date):
        return 541

    def getDislikesCountOnDate(self, date):
        return 149





