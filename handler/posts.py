from flask import jsonify
from dao.posts import PostsDao


class postHandler:


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
        p1={}
        p1['postId'] = 1
        p1['photoId'] = "265A2"
        p1['caption'] = "Some inspiring caption"
        p1['postDate'] = '2/14/2018 15:00:00'
        p1['userId'] = '1'
        p1['chatId'] = '1'
        
        p2={}
        p2['postId'] = 2
        p2['photoId'] = "542B1"
        p2['caption'] = "Yesterday in Condado!"
        p2['postDate'] = '2/17/2018 10:00:00'
        p2['userId'] = '2'
        p2['chatId'] = '1'
        
        p3={}
        p3['postId'] = 3
        p3['photoId'] = "21476"
        p3['caption'] = "Some inspiring caption"
        p3['postDate'] = '2/14/2018 15:00:00'
        p3['userId'] = '1'
        p3['chatId'] = '1'

        postsList = []
        postsList.append(p1)
        postsList.append(p2)
        postsList.append(p3)
        return jsonify(Posts=postsList)

    def getPostsByChatId(self, chatId):
        if(chatId == 1):
            p1 = {}
            p1['postId'] = 1
            p1['photoId'] = "265A2"
            p1['caption'] = "Some inspiring caption"
            p1['postDate'] = '2/14/2018 15:00:00'
            p1['userId'] = '1'
            p1['chatId'] = '1'

            p2 = {}
            p2['postId'] = 2
            p2['photoId'] = "542B1"
            p2['caption'] = "Yesterday in Condado!"
            p2['postDate'] = '2/17/2018 10:00:00'
            p2['userId'] = '2'
            p2['chatId'] = '1'

            postsList = []
            postsList.append(p1)
            postsList.append(p2)
            return jsonify(Post=postsList)

        elif(chatId == 2):
            p3 = {}
            p3['postId'] = 3
            p3['photoId'] = "21476"
            p3['caption'] = "Some inspiring caption"
            p3['postDate'] = '2/14/2018 15:00:00'
            p3['userId'] = '1'
            p3['chatId'] = '2'

            postsList = []
            postsList.append(p3)
            return jsonify(Post=postsList)

        else:
            return 'There is no chat group with id %d' %chatId

    def insertPost(self, json):
        photoId = json('photoId')
        caption = json('caption')
        postDate = json('postDate')
        userId = json('userId')
        chatId = json('chatId')
        if photoId and caption and postDate and userId and chatId:
            dao = PostsDao()
            pid = dao.insert(photoId, caption, postDate, userId, chatId)
            result = self.build_part_attributes(photoId, caption, postDate, userId, chatId)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


