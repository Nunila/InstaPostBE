from flask import jsonify
from dao.person import PersonDAO

class PersonsHandler:

    def buildPersonAttributes(self, row):
        result = {}
        result['personId'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]
        result['phoneNumber'] = row[3]
        result['email'] = row[4]
        result['birthday'] = row[5]
        return result

    def getAllPersons(self):
        dao = PersonDAO()
        person_list = dao.getAllPersons()
        return jsonify(person_list), 200

    def getPersonById(self, perid):
        dao = PersonDAO()
        person = dao.getPersonByID(perid)
        return jsonify(person), 200

    def getPersonByArguments(self, args):
        dao = PersonDAO()
        person_list = dao.getPersonByFullName(args)
        return jsonify(person_list), 200

    def addConctact(self, ownerid, perid):
        dao = PersonDAO()
        response = dao.addContact(ownerid, perid)
        return jsonify(response=response), 200

    def deleteContact(self, ownerid, perid):
        dao = PersonDAO()
        status = dao.deleteContact(ownerid, perid)
        return jsonify(DeleteStatus=status), 200

    def insertPersonJson(self, json):
        dao = PersonDAO()
        new_person = dao.insert(json)
        return jsonify(new_person), 200

    def updatePerson(self, perid, form):
        dao = PersonDAO()
        updated_person = dao.update(perid, form)
        return jsonify(updated_person), 200

    def deletePerson(self, perid):
        dao = PersonDAO()
        id = dao.delete(perid)
        return jsonify(DeleteStatus='OK'), 200

