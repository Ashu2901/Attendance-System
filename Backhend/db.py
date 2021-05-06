import mysql.connector


def connection():
    db = mysql.connector.connect(host='localhost', user='root', passwd='sparrow',
                                 database='attendschema', auth_plugin='mysql_native_password')
    cursor = db.cursor()
    return db, cursor
