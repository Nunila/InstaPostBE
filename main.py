from flask import Flask, jsonify, request
from handler.chats import ChatHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin


# Activate
app = Flask(__name__)

# Apply CORS to this app
CORS(app)


@app.route('/')
@cross_origin()
def greeting():
    return 'Hello, this is the InstaPost DB App!'


@app.route('/InstaPost/chats', methods=['GET', 'POST'])
def getAllChats():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().insertChatJson(request.json)
    else:
        if not request.args:
            return ChatHandler().getAllChats()
        else:
            return ChatHandler().searchChats(request.args)

@app.route('/InstaPost/chats/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def getChatById(cid):
    if request.method == 'GET':
        return ChatHandler().getChatById(cid)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(cid, request.form)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(cid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaPost/chats/<int:uid>/member', methods=['GET'])
def getChatByMemberId(uid):
    if request.method == 'GET':
        return ChatHandler().getChatsByMemberId(uid)
    else:
        return jsonify(Error="Method not allowed."), 405


#----------------------------Original---------------------------------


# @app.route('/PartApp/parts', methods=['GET', 'POST'])
# def getAllParts():
#     if request.method == 'POST':
#         # cambie a request.json pq el form no estaba bregando
#         # parece q estaba poseido por satanas ...
#         # DEBUG a ver q trae el json q manda el cliente con la nueva pieza
#         print("REQUEST: ", request.json)
#         return PartHandler().insertPartJson(request.json)
#     else:
#         if not request.args:
#             return PartHandler().getAllParts()
#         else:
#             return PartHandler().searchParts(request.args)
#
#
# @app.route('/PartApp/parts/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
# def getPartById(pid):
#     if request.method == 'GET':
#         return PartHandler().getPartById(pid)
#     elif request.method == 'PUT':
#         return PartHandler().updatePart(pid, request.form)
#     elif request.method == 'DELETE':
#         return PartHandler().deletePart(pid)
#     else:
#         return jsonify(Error="Method not allowed."), 405
#
#
# @app.route('/PartApp/parts/<int:pid>/suppliers')
# def getSuppliersByPartId(pid):
#     return PartHandler().getSuppliersByPartId(pid)
#
#
# @app.route('/PartApp/suppliers', methods=['GET', 'POST'])
# def getAllSuppliers():
#     if request.method == 'POST':
#         return SupplierHandler().insertSupplier(request.form)
#     else :
#         if not request.args:
#             return SupplierHandler().getAllSuppliers()
#         else:
#             return SupplierHandler().searchSuppliers(request.args)
#
#
# @app.route('/PartApp/suppliers/<int:sid>',
#            methods=['GET', 'PUT', 'DELETE'])
# def getSupplierById(sid):
#     if request.method == 'GET':
#         return SupplierHandler().getSupplierById(sid)
#     elif request.method == 'PUT':
#         pass
#     elif request.method == 'DELETE':
#         pass
#     else:
#         return jsonify(Error = "Method not allowed"), 405
#
#
# @app.route('/PartApp/suppliers/<int:sid>/parts')
# def getPartsBySuplierId(sid):
#     return SupplierHandler().getPartsBySupplierId(sid)
#
#
# @app.route('/PartApp/parts/countbypartid')
# def getCountByPartId():
#     return PartHandler().getCountByPartId()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
