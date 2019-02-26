from config import dbconfig
#import psycopg2

class PersonDAO:

    personArray = [{"ownerID":1, "firstName":"Homero", "lastName":"Simpson", "phone":"1234567890",
                    "email":"homerS@gmail.com", "birthday": "12/23/1968"},
                   {"contactID": 2, "firstName": "JoJo", "lastName": "Jojo", "phone": "123454290",
                    "email": "jojoreference@gmail.com", "birthday": "01/01/1968"}]

    def getAllPersons(self):
        return self.personArray

    def getPersonByID(self, perid):
        return self.personArray[0]

    def getPersonByFName(self, perfname):
        return self.personArray[1]

    def getPersonByLName(self, perlname):
        return self.personArray[2]

    def getPersonByFullName(self, perfname, perlname):
        return self.personArray[1], self.personArray[2]

    def addContact(self, ownerid, perid):
        return 'Contact added successfully.'

    def deleteContact(self, ownerid, perid):
        return 'Conctact deleted successfully.'

    def insert(self, json):
        return self.personArray[1]

    def update(self, perid, form):
        return self.personArray[1]

    def delete(self, perid):
        return perid