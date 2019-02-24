from flask import jsonify
from dao.posts import PostsDAO


class PostHandler:


    def buildPostDict(self, row):
        result = {}
        result['postId'] = row[0]
        result['photoId'] = row[1]
        result['caption'] = row[2]
        result['postDate'] = row[3]
        result['userId'] = row[4]
        result['chatId'] = row[5]
        return result

    def buildPostAttributes(self, postId, photoId, caption, postDate, userId, chatId):
        result = {}
        result['postId'] = postId
        result['photoId'] = photoId
        result['caption'] = caption
        result['postDate'] = postDate
        result['userId'] = userId
        result['chatId'] = chatId
        return result

#---------------Operations---------------------------------------------------------

    def getAllPosts(self):
        dao = PostsDAO()
        posts_List = dao.getAllPosts()
        return jsonify(posts_List)

    def getPostById(self, postId):
        dao = PostsDAO()
        posts_List = dao.getPostById(postId)
        return jsonify(posts_List)

    def getPostsByChatId(self, chatId):
        dao = PostsDAO()
        posts_List = dao.getPostsByChatId(chatId)
        return jsonify(posts_List)

    def getNumOfPostsByDate(self, date):
        dao = PostsDAO()
        numOfPosts = dao.getNumOfPostsByDate(date)
        return jsonify(numOfPosts)

    def insertPost(self, json):
        dao = PostsDAO()
        newPost = dao.insertPost(json)
        return jsonify(newPost)

    def updatePost(self, postId, form):
        dao = PostsDAO()
        updatePost = dao.updatePost(postId, form)
        return jsonify(updatePost)

    def deletePost(self, postId):
        dao = PostsDAO()
        id = dao.deletePost(PostId)
        return jsonify(DeleteStatus="OK"), 200

