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

    def getPostsByChatId(self, chatId):
        dao = PostsDAO()
        posts_List = dao.getPostsByChatId(chatId)
        return jsonify(posts_List)

    def insertPost(self, json):
        dao = PostsDAO()
        newPost = dao.insert(json)
        return jsonify(newPost)

    def updateReaction(self, cid, form):
        dao = PostsDAO()
        updatePost = dao.update(cid, form)
        return jsonify(updatePost)

    def deleteReaction(self, cid):
        dao = PostsDAO()
        id = dao.delete(cid)
        return jsonify(DeleteStatus="OK"), 200

