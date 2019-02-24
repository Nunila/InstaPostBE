from flask import jsonify
from dao import personDAO

class PersonsHandler:

    def getAllPersons(self):
        dao = personDAO()
        person_list = dao.getAllPersons()
        return jsonify(person_list)

    def getPersonByID(self, perid):
        dao = personDAO()
        person = dao.getPersonByID(perid)
        return jsonify(person)

    def getPersonByFName(self, pfname):
        dao = personDAO()
        person_list = dao.getPersonByFName(pfname)
        return jsonify(person_list)

    def getPersonByLName(self, plname):
        dao = personDAO()
        person_list = dao.getPersonByLName(plname)
        return jsonify(person_list)

    def getPersonByFullName(self, pfname, plname):
        dao = personDAO()
        person_list = dao.getPersonByFullName(pfname, plname)
        return jsonify(person_list)

    def getPersonByEmail(self, permail):
        dao = personDAO()
        person_list = dao.getPersonByEmail(permail)
        return jsonify(person_list)

    def insertPersonJson(self, json):
        dao = personDAO()
        new_person = dao.insert(json)
        return jsonify(new_person)

    def updatePerson(self, perid, form):
        dao = personDAO()
        updated_person = dao.update(perid, form)
        return jsonify(updated_person)

    def deletePerson(self, perid):
        dao = personDAO()
        id = dao.delete(perid)
        return jsonify(DeleteStatus = "OK"), 200