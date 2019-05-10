from config.dbconfig import pg_config
import psycopg2

class UsersDAO:

    userArray = [{"userId": 1, "userName": 'Homero123', "password": 'dotdashdot'},
                 {"userId": 2, "userName": 'Salchicha2', "password": 'bootwoot9'}]

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'],
                                                                           pg_config['host']
                                                                           )

        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select userId, username, personId, firstName, lastName, phoneNumber, email, birthday from Users natural inner join Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByID(self, uid):
        cursor = self.conn.cursor()
        query = "select userId, username, personId, firstName, lastName, phoneNumber, email, birthday from Users natural inner join Person where userid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserByUName(self, uname):
        cursor = self.conn.cursor()
        query = "select * from (select userId, username, personId, firstName, lastName, phoneNumber, email, birthday " \
                "from Users natural inner join Person where Person.userid = Users.userid) as foo where foo.userName = %s;"
        cursor.execute(query, (uname,))
        result = cursor.fetchone()
        return result

    def getUserLogin(self, username, password):
        cursor = self.conn.cursor()
        query = "select * from (select userId, username, password, personId, firstName, lastName, phoneNumber, email, birthday " \
                "from Users natural inner join Person where Person.userid = Users.userid) as foo where foo.userName = %s and foo.password = %s;"
        cursor.execute(query, (username, password,))
        result = cursor.fetchone()#return person info using user ID pa el handler hacer el dictionary y pa lante
        return result

    def getMostActiveUsersByDate(self):
        cursor = self.conn.cursor()
        query = "select userid, date(messagedate), count(*) as numberOfMessages, username " \
                "from message natural inner join users group by date(messagedate), userid, username " \
                "order by date(messagedate) desc, count(*) desc;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, json):
        username = json['userName']
        password = json['password']
        cursor = self.conn.cursor()
        query = "insert into Users(username, password) values (%s, %s) returning userId;"
        cursor.execute(query, (username, password,))
        self.conn.commit()
        uId = cursor.fetchone()
        if not uId:
            return uId
        else:
            fname = json['firstName']
            lname = json['lastName']
            pnum = json['phoneNum']
            email = json['email']
            bday = json['birthday']
            userId = uId
            query = "insert into Person(firstName, lastName, phoneNumber, email, birthday, userId) values (%s, %s, %s, %s, %s, %s) returning personId;"
            cursor.execute(query, (fname, lname, pnum, email, bday, userId,))
            self.conn.commit()
            return userId

    def update(self, userId, username, password):
        cursor = self.conn.cursor()
        query = "update Users set username = %s, password = %s where userId = %s;"
        cursor.execute(query, (username, password, userId,))
        self.conn.commit()
        return userId

    def delete(self, uid):
        cursor = self.conn.cursor()
        query = "delete from Users where userId = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid

