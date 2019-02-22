
import datetime


class ChatsDAO:

    chatArray = [{"chatId": 1, "chatName": 'DBProject', "creationDate": datetime.datetime.now(), "chatOwnerId": 4},
                 {"chatId": 2, "chatName": 'Family', "creationDate": datetime.datetime.now(), "chatOwnerId": 5},
                 {"chatId": 3, "chatName": 'Game of Thrones viewing party', "creationDate": datetime.datetime.now(), "chatOwnerId": 1},
                 {"chatId": 4, "chatName": 'Capstone', "creationDate": datetime.datetime.now(), "chatOwnerId": 8},
                 {"chatId": 5, "chatName": 'BestFriends', "creationDate": datetime.datetime.now(), "chatOwnerId": 5}]

    def getAllChats(self):
        return self.chatArray

    def getChatById(self, pid):
        return self.chatArray[0]

    def getChatsByArgs(self, args):
        return [self.chatArray[1], self.chatArray[2]]

    def getChatsByMemberId(self, uid):
        return [self.chatArray[3], self.chatArray[4]]

    def insert(self, json):
        return self.chatArray[2]

    def update(self, pid, form):
        return self.chatArray[4]

    def delete(self, pid):
        return pid





