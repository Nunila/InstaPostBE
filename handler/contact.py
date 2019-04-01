from flask import jsonify
from dao.contact import ContactDAO


class ContactHandler:

    def buildContactDict(self, row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['phonenumber'] = row[2]
        result['email'] = row[3]
        result['birthday'] = row[4]
        result['username'] = row[5]
        return result

#----------------------Operations---------------------

    def getContactsOfPerson(self, pid):
        dao = ContactDAO()
        person_list = dao.getContactsOfPerson(pid)
        result_list = []
        for row in person_list:
            result = self.buildContactDict(row)
            result_list.append(result)

        return jsonify(Contacts = result_list), 200