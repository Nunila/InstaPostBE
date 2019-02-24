
class PostsDAO:

    postsArray = [{"postId": 1, "photoId": '345C6', "postDate": '2/21/2019 12:00:00'},
                  {"postId": 2, "photoId": '265A2', "postDate": '2/14/2018 15:00:00'},
                  {"postId": 3, "photoId": '542B1', "postDate": '2/17/2019 21:00:00'},
                  {"postId": 4, "photoId": '21476', "postDate": '2/23/2019 11:00:00'},
                  {"postId": 5, "photoId": '635W9', "postDate": '5/01/2019 4:00:00'}]

    def getAllPosts(self):
        return self.postsArray

    def getPostById(self, postId):
        return self.postsArray[0]

    def getPostsByUserId(self, userId):
        return self.postsArray[0]

    def getPostsByChatId(self, chatId):
        return self.postsArray

    def getPostsByDate(self, postDate):
        return self.postsArray[4]

    def getNumOfPostsByDateAndUser(self, date, userId):
        return 8

    def getNumOfPostsByDate(self, date):
        return 100

    def insertPost(self, photoId, postDate):
        return 'Succesfully inserted new post!'

    def updatePost(self, postId):
        return self.postsArray[2]

    def deletePost(self, postId):
        return 'Sucessfully deleted!'


