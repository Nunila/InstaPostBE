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
        result['userId'] = row[6]
        return result

    def buildPersonAndUserAttributes(self, row):
        result = {}
        result['personId'] = row[0]
        result['firstName'] = row[1]
        result['lastName'] = row[2]
        result['phoneNumber'] = row[3]
        result['email'] = row[4]
        result['birthday'] = row[5]
        result['userId'] = row[6]
        result['username'] = row[7]
        result['password'] = row[8]
        return result

    def buildPersonDict(self, userId, pid, firstname, lastname, phonenumber,email, birthday):
        result = {}
        result['personId'] = pid
        result['firstName'] = firstname
        result['lastName'] = lastname
        result['phonenumber'] = phonenumber
        result['email'] = email
        result['birthday'] = birthday
        result['userId'] = userId
        return result

    def getAllPersons(self):
        dao = PersonDAO()
        person_list = dao.getAllPersons()
        return jsonify(person_list), 200

    def getPersonById(self, perid):
        dao = PersonDAO()
        row = dao.getPersonByID(perid)
        if not row:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.buildPersonAttributes(row)

        return jsonify(person), 200

    def getPersonAndUserById(self, perid):
        dao = PersonDAO()
        row = dao.getPersonAndUserByID(perid)
        if not row:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.buildPersonAndUserAttributes(row)

        return jsonify(person), 200

    def getPersonByArguments(self, args):
        dao = PersonDAO()
        email = args.get("email")
        phone = args.get("phonenumber")

        if (len(args) == 1) and phone:
            row = dao.getPersonByPhoneNumber(phone)
        elif (len(args) == 1) and email:
            row = dao.getPersonByEmail(email)
        else:
            return jsonify(Error="Malformed query string"), 400

        if not row:
            return jsonify(Error="Person Not Found"), 404
        else:
            person = self.buildPersonAttributes(row)
            return jsonify(person), 200

    def addConctact(self, ownerid, perid):
        dao = PersonDAO()
        response = dao.addContact(ownerid, perid)
        return jsonify(response=response), 200

    def deleteContact(self, ownerid, perid):
        dao = PersonDAO()
        status = dao.deleteContact(ownerid, perid)
        return jsonify(DeleteStatus=status), 200

    def insertPerson(self, json):
        firstname = json['firstName']
        lastname = json['lastName']
        phonenumber = json['phonenumber']
        email = json['email']
        birthday = json['birthday']
        userId = json['userId']

        # if userId and firstname and lastname and phonenumber and email and birthday:
        dao = PersonDAO()
        pid = dao.insert(userId, firstname, lastname, phonenumber,email, birthday)
        result = self.buildPersonDict(userId, pid, firstname, lastname, phonenumber, email, birthday)

        return jsonify(result), 201
        # else:
        #
        #     return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePerson(self, perid, form):
        dao = PersonDAO()
        updated_person = dao.update(perid, form)
        return jsonify(updated_person), 200

    def deletePerson(self, perid):
        dao = PersonDAO()
        id = dao.delete(perid)
        return jsonify(DeleteStatus='OK'), 200

