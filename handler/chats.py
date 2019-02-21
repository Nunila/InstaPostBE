from flask import jsonify
from dao.chats import ChatsDAO

import datetime


class ChatHandler:

    def build_chat_attributes(self, cid, cname, cowner, date):
        result = {}
        result['chatId'] = cid
        result['chatName'] = cname
        result['chatOwnerId'] = cowner
        result['creationDate'] = date
        return result

#-------------------------Modifications-----------------------------
    def getAllChats(self):
        dao = ChatsDAO()
        chats_list = dao.getAllChats()
        return jsonify(chats_list)
        # result_list = []
        # for row in parts_list:
        #     result = self.build_part_dict(row)
        #     result_list.append(result)
        #     return jsonify(result_list)
        # return jsonify(Parts=result_list)

    def getChatById(self, cid):
        dao = ChatsDAO()
        row = dao.getChatById(cid)
        return jsonify(row)


    def searchChats(self, args):
        chatName = args.get("chatName")
        creationDate = args.get("creationDate")
        dao = ChatsDAO()
        chats_list = []
        if (len(args) == 2) and chatName and creationDate:
            chats_list = dao.getChatsByNameAndDate(chatName,creationDate)
        elif (len(args) == 1) and chatName:
            chats_list = dao.getChatsByName(chatName)
        elif (len(args) == 1) and creationDate:
            chats_list = dao.getChatsByCreationDate(creationDate)
        else:
            return jsonify(Error = "Malformed query string"), 400
        # result_list = []
        # for row in chats_list:
        #     result = self.build_chat_dict(row)
        #     result_list.append(result)
        # return jsonify(Parts=result_list)
        return jsonify(chats_list)

    def getChatsByMemberId(self, uid):
        dao = ChatsDAO()
        chats_list = []
        chats_list = dao.getChatsByMemberId(uid)
        # result_list = []
        # for row in chats_list:
        #     result = self.build_chatt_dict(row)
        #     result_list.append(result)
        # return jsonify(Parts=result_list)
        return chats_list

    def getChatsByOwnerId(self, uid):
        dao = ChatsDAO()
        chats_list = []
        chats_list = dao.getChatsByOwnerId(uid)
        # result_list = []
        # for row in chats_list:
        #     result = self.build_chatt_dict(row)
        #     result_list.append(result)
        # return jsonify(Parts=result_list)
        return chats_list

    # def getSuppliersByPartId(self, pid):
    #     dao = ChatsDAO()
    #     if not dao.getPartById(pid):
    #         return jsonify(Error="Part Not Found"), 404
    #     suppliers_list = dao.getSuppliersByPartId(pid)
    #     result_list = []
    #     for row in suppliers_list:
    #         result = self.build_supplier_dict(row)
    #         result_list.append(result)
    #     return jsonify(Suppliers=result_list)

    # def insertChat(self, form):
    #     print("form: ", form)
    #     date = datetime.datetime.now()
    #     # If form does not have all fields, being: chatOwnerId,chatName and at least one other member. Creation date
    #     # is automatically filled.
    #     if len(form) != 3:
    #         return jsonify(Error = "Malformed post request"), 400
    #     else:
    #         cname = form['chatName']
    #         cOwnerId = form['chatOwnerId']
    #         # Members is an array where the first index is the owner id
    #         members = form['chatMembers']
    #         if cname and cOwnerId and members:
    #             dao = ChatsDAO()
    #             cid = dao.insert(cname, cOwnerId, date.isoformat())
    #             result = self.build_chat_attributes(cid, cname, cOwnerId, date.isoformat())
    #             return jsonify(result), 201;
    #             # return jsonify(Part=result), 201
    #         else:
    #             return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def insertChatJson(self, json):
    #
    #     date = datetime.datetime.now()
    #     cname = json['chatName']
    #     cOwnerId = json['chatOwnerId']
    #     # Members is an array where the first index is the owner id
    #     members = json['chatMembers']
    #     if cname and cOwnerId and members:
    #         dao = ChatsDAO()
    #         cid = dao.insert(cname, cOwnerId, date.isoformat())
    #         result = self.build_chat_attributes(cid, cname, cOwnerId, date.isoformat())
    #         return jsonify(result), 201
    #         # return jsonify(Part=result), 201
    #     else:
    #         return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def deletePart(self, pid):
    #     dao = ChatsDAO()
    #     if not dao.getPartById(pid):
    #         return jsonify(Error = "Part not found."), 404
    #     else:
    #         dao.delete(pid)
    #         return jsonify(DeleteStatus = "OK"), 200
    #
    # def updatePart(self, pid, form):
    #     dao = ChatsDAO()
    #     if not dao.getPartById(pid):
    #         return jsonify(Error = "Part not found."), 404
    #     else:
    #         if len(form) != 4:
    #             return jsonify(Error="Malformed update request"), 400
    #         else:
    #             pname = form['pname']
    #             pprice = form['pprice']
    #             pmaterial = form['pmaterial']
    #             pcolor = form['pcolor']
    #             if pcolor and pprice and pmaterial and pname:
    #                 dao.update(pid, pname, pcolor, pmaterial, pprice)
    #                 result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
    #                 return jsonify(Part=result), 200
    #             else:
    #                 return jsonify(Error="Unexpected attributes in update request"), 400
    #
    # def build_part_counts(self, part_counts):
    #     result = []
    #     #print(part_counts)
    #     for P in part_counts:
    #         D = {}
    #         D['id'] = P[0]
    #         D['name'] = P[1]
    #         D['count'] = P[2]
    #         result.append(D)
    #     return result
    #
    # def getCountByPartId(self):
    #     dao = ChatsDAO()
    #     result = dao.getCountByPartId()
    #     #print(self.build_part_counts(result))
    #     return jsonify(PartCounts = self.build_part_counts(result)), 200






