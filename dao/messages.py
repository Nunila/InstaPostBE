class MessagesDAO:
    
    messagesArray=[{"messageId": 1, "content": 'Insert inspiring caption here', "messageDate": '2/21/2019 12:00:00', "messageType": 'caption'},
                   {"messageId": 2, "content": 'I love your photo!', "messageDate": '2/21/2019 14:00:00', "messageType": 'reply'}]

    def getAllMessages(self):
        return self.messagesArray

    def getMessageById(self, messageId):
        return self.messagesArray

    def getMessagesByUserId(self, userId):
        return self.messagesArray

    def getMessagesByChatId(self, chatId):
        return self.messagesArray

    def getMessagesByDate(self, messageDate):
        return self.messagesArray

    def getNumOfRepliesByDate(self, date):
        return 100

    def getNumOfRepliesByDateAndPost(self, date, postId):
        return 20

    def insertMessage(self,json):
        return 'Succesfully inserted new post!'

    def updateMessage(self, json):
        return self.messagesArray

    def deleteMessage(self, json):
        return 'Sucessfully deleted!'