from config.dbconfig import pg_config
import psycopg2


class ContactDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'],
                                                                           pg_config['host']
                                                                           )

        self.conn = psycopg2._connect(connection_url)

    personArray = [{"ownerID":1, "firstName":"Homero", "lastName":"Simpson", "phone":"1234567890",
                    "email":"homerS@gmail.com", "birthday": "12/23/1968"},
                   {"contactID": 2, "firstName": "JoJo", "lastName": "Jojo", "phone": "123454290",
                    "email": "jojoreference@gmail.com", "birthday": "01/01/1968"}]

    def getContactsOfPerson(self, pid):
        cursor = self.conn.cursor()
        query = "select firstname, lastname, phonenumber, email, birthday, username, userid, personid " \
                "from users as U natural inner join " \
                "(contacts as C inner join Person as P on P.personid = C.contactid ) " \
                "where C.ownerid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
