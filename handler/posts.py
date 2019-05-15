from flask import jsonify
from dao.posts import PostsDAO
from handler.messages import MessageHandler
import datetime


class PostHandler:

    def buildPostDict(self, row):
        result = {}
        result['postId'] = row[0]
        result['userId'] = row[1]
        result['messageId'] = row[2]
        result['chatId'] = row[3]
        result['photourl'] = row[4]
        result['postDate'] = row[5]
        result['content'] = row[6]
        result['username'] = row[7]

        return result

    def buildPostDict2(self, row):
        result = {}
        result['postId'] = row[0]
        result['chatId'] = row[1]
        result['userId'] = row[2]
        result['photourl'] = row[3]
        result['messageId'] = row[4]
        result['content']= row[5]
        result['postDate'] = row[6]
        result['username'] = row[7]
        return result

    def buildPostPerDayDict(self, row):
        result = {}
        result['day'] = row[0]
        result['total'] = row[1]
        return result

    def buildPostDictDashboard(self, row):
        result = {}
        result['postId'] = row[0]
        result['caption'] = row[1]
        return result

    def buildPostAttributes(self, postId, chatId, userId, messageId, photourl, postDate):
        result = {}
        result['postId'] = postId
        result['chatId'] = chatId
        result['userId'] = userId
        result['messageId'] = messageId
        result['photourl'] = photourl
        result['postDate'] = postDate
        return result

#---------------Operations---------------------------------------------------------

    def getAllPosts(self):
        dao = PostsDAO()
        posts_List = dao.getAllPosts()
        result_list = []
        for row in posts_List:
            result = self.buildPostDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getAllPostsForDashboard(self):
        dao = PostsDAO()
        posts_List = dao.getAllPostsForDashboard()
        result_list = []
        for row in posts_List:
            result = self.buildPostDictDashboard(row)
            result_list.append(result)

        return jsonify(result_list)


    def getPostById(self, postId):
        dao = PostsDAO()
        posts_List = dao.getPostById(postId)
        result_list = []
        for row in posts_List:
            result = self.buildPostDict2(row)
            result_list.append(result)

        return jsonify(result_list)

    def getPostsByChatId(self, chatId):
        dao = PostsDAO()
        posts_List = dao.getPostsByChatId(chatId)
        result_list = []
        for row in posts_List:
            result = self.buildPostDict2(row)
            result_list.append(result)

        return jsonify(result_list)

    def getPostsByUserId(self, userId):
        dao = PostsDAO()
        posts_List = dao.getPostsByUserId(userId)
        result_list = []
        for row in posts_List:
            result = self.buildPostDict2(row)
            result_list.append(result)

        return jsonify(result_list)

    def getPostsByDate(self, postDate):
        dao = PostsDAO()
        posts_List = dao.getPostsByDate(postDate)
        result_list = []
        for row in posts_List:
            result = self.buildPostDict2(row)
            result_list.append(result)

        return jsonify(result_list)

    def getNumberOfPostsPerDay(self):
        dao = PostsDAO()
        posts_List = dao.getNumberOfPostsPerDay()
        result_list = []
        for row in posts_List:
            result = self.buildPostPerDayDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def getNumOfPostsByDate(self, date):
        dao = PostsDAO()
        numOfPosts = dao.getNumOfPostsByDate(date)
        return jsonify(numOfPosts)

    def getNumOfPostsByDateOfUser(self, userId):
        dao = PostsDAO()
        posts = dao.getNumOfPostsByDateOfUser(userId)
        result_list = []
        for row in posts:
            result = self.buildPostPerDayDict(row)
            result_list.append(result)

        return jsonify(result_list)

    def insertPost(self, json):
        chatId = json['chatId']
        userId = json['userId']
        messageHandler = MessageHandler()
        messageId = messageHandler.insertMessage(json)[0]
        photourl = str(json['src'])
        postDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if chatId and userId and messageId and photourl and postDate:
            dao = PostsDAO()
            postId = dao.insertPost(chatId, userId, messageId, photourl, postDate)
            result = self.buildPostAttributes(postId, chatId, userId, messageId, photourl, postDate)
            return jsonify(result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePost(self, postId, form):
        dao = PostsDAO()
        updatePost = dao.updatePost(postId, form)
        return jsonify(updatePost)

    def deletePost(self, postId):
        dao = PostsDAO()
        id = dao.deletePost(postId)
        return jsonify(DeleteStatus="OK"), 200

