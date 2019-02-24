from config import dbconfig
import psycopg2

class PersonDAO:

    personArray = [{"personID":1, "firstName":"Homero", "lastName":"Simpson", "phone":"1234567890", "email":"homerS@gmail.com",
                   "birthday": "12/23/1968"}]

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

    def getPersonByEmail(self, permail):
        return self.personArray[4]

    def insert(self, json):
        return self.personArray[1]

    def update(self, perid, form):
        return self.personArray[1]

    def delete(self, perid):
        return perid