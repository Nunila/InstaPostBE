from config import dbconfig
import psycopg2

class PersonDAO:

    personArray = [{"ownerID":1, "firstName":"Homero", "lastName":"Simpson", "phone":"1234567890",
                    "email":"homerS@gmail.com", "birthday": "12/23/1968"},
                   {"contactID": 2, "firstName": "JoJo", "lastName": "Jojo", "phone": "123454290",
                    "email": "jojoreference@gmail.com", "birthday": "01/01/1968"}]

    def _init_(self):
        connectionURL="dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                         dbconfig['user'],
                                                         dbconfig['passwd'])

        self.conn = psycopg2._connect(connectionURL)

    def getAllPersons(self):
        cursor = self.conn.cursor()
        query = "select * from Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonByID(self, perid):
        cursor = self.conn.cursor()
        query = "select * from Person where personId = %s;"
        cursor.execute(query, (perid,))
        result = cursor.fetchone()
        return result

    def getPersonByFName(self, perfname):
        cursor = self.conn.cursor()
        query = "select * from Person where firstName = %s;"
        cursor.execute(query, (perfname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonByLName(self, perlname):
        cursor = self.conn.cursor()
        query = "select * from Person where lastName = %s;"
        cursor.execute(query, (perlname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonByFullName(self, perfname, perlname):
        cursor = self.conn.cursor()
        query = "select * from Person where firstName = %s and lastName = %s;"
        cursor.execute(query, (perfname, perlname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, fname, lname, pnum, email, bday):
        cursor = self.conn.cursor()
        query = "insert into Person(firstName, lastName, phoneNumber, email, birthday) values (%s, %s, %s, %s, %s) returning personId;"
        cursor.execute(query, (fname, lname, pnum, email, bday,))
        perid = cursor.fetchone()[0]
        self.conn.commit()
        return perid

    def update(self, perid, fname, lname, pnum, email, bday):
        cursor = self.conn.cursor()
        query = "update Person set firstName = %s, lastName = %s, phoneNumber=%s, email-%s, birthday=%s where personId = %s;"
        cursor.execute(query, (fname, lname, pnum, email, bday, perid,))
        self.conn.commit()
        return perid

    def delete(self, perid):
        cursor = self.conn.cursor()
        query = "delete from Person where personId = %s;"
        cursor.execute(query, (perid,))
        self.conn.commit()
        return perid