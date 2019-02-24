from config import dbconfig
import psycopg2

class PersonDAO:

    personArray = [{"personID":1, "firstName":"Homero", "lastName":"Simpson", "phone":"1234567890", "email":"homerS@gmail.com", }]