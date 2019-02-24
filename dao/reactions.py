
import datetime


class ReactionsDAO:

    reactionArray = [{"reactionId": 1, "userId": 2, "postId": 7, "messageId": '', "type": 'like', "date": datetime.datetime.now()},
                 {"reactionId": 2, "userId": 8, "postId": 4, "messageId": 3, "type": 'dislike', "date": datetime.datetime.now()},
                 {"reactionId": 3, "userId": 12, "postId": 11, "messageId": 25, "type": 'like', "date": datetime.datetime.now()},
                 {"reactionId": 4, "userId": 2, "postId": 8, "messageId": 18, "type": 'dislike', "date": datetime.datetime.now()},
                 {"reactionId": 5, "userId": 33, "postId": 50, "messageId": '', "type": 'like', "date": datetime.datetime.now()}]

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





