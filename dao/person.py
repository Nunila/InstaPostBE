import psycopg2
from config.dbconfig import pg_config


class PersonDAO:

    personArray = [{"ownerID":1, "firstName":"Homero", "lastName":"Simpson", "phone":"1234567890",
                    "email":"homerS@gmail.com", "birthday": "12/23/1968"},
                   {"contactID": 2, "firstName": "JoJo", "lastName": "Jojo", "phone": "123454290",
                    "email": "jojoreference@gmail.com", "birthday": "01/01/1968"}]

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'],
                                                                           pg_config['host']
                                                                           )

        self.conn = psycopg2._connect(connection_url)


    def getAllPersons(self):
        cursor = self.conn.cursor()
        query = "select * from Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonByEmail(self, peremail):
        cursor = self.conn.cursor()
        query = "select * from Person where email = %s;"
        cursor.execute(query, (peremail,))
        result = cursor.fetchone()
        return result

    def getPersonByPhoneNumber(self, perphone):
        cursor = self.conn.cursor()
        query = "select * from Person where phonenumber = %s;"
        cursor.execute(query, (perphone,))
        result = cursor.fetchone()
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

    def getUsernameByPersonId(self, perid):
        cursor = self.conn.cursor()
        query = "select userId, userName from Person natural inner join Users where personId = %s;"
        cursor.execute(query, (perid,))
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