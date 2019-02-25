from flask import jsonify
from dao.personDAO import PersonDAO

class PersonsHandler:

    def getAllPersons(self):
        dao = PersonDAO()
        person_list = dao.getAllPersons()
        return jsonify(person_list)

    def getPersonById(self, perid):
        dao = PersonDAO()
        person = dao.getPersonByID(perid)
        return jsonify(person)

    def getPersonByFName(self, pfname):
        dao = PersonDAO()
        person_list = dao.getPersonByFName(pfname)
        return jsonify(person_list)

    def getPersonByLName(self, plname):
        dao = PersonDAO()
        person_list = dao.getPersonByLName(plname)
        return jsonify(person_list)

    def getPersonByFullName(self, pfname, plname):
        dao = PersonDAO()
        person_list = dao.getPersonByFullName(pfname, plname)
        return jsonify(person_list)

    def getPersonByEmail(self, permail):
        dao = PersonDAO()
        person_list = dao.getPersonByEmail(permail)
        return jsonify(person_list)

    def insertPersonJson(self, json):
        dao = PersonDAO()
        new_person = dao.insert(json)
        return jsonify(new_person)

    def updatePerson(self, perid, form):
        dao = PersonDAO()
        updated_person = dao.update(perid, form)
        return jsonify(updated_person)

    def deletePerson(self, perid):
        dao = PersonDAO()
        id = dao.delete(perid)
        return jsonify(DeleteStatus = "OK"), 200