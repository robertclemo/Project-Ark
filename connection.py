import mysql.connector
# import python_mysql_dbconfig
from mysql.connector import connect, Error, MySQLConnection
# from python_mysql_dbconfig import read_dn_config

cnx = mysql.connector.connect(user='admin', password='Phipsy1!',
                              host='127.0.0.1',
                              database='practice')
cnx.close()




def query_with_fetchone():
    try:
        dbconfig = read_dn_config()
        
        conn = MySQLConnection(**dbconfig)
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM cats")

        row = cursor.fetchone()

        while row is not None:
            print(row)

            row = cursor.fetchone()

    except Error as e:
        print(e)
    

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchone



conn = connect(
        host='127.0.0.1',
        user='admin',
        password='Phipsy1!',
        database='practice'
)

try:
    cursor = conn.cursor()
    cursor.execute('select * from cats')

    for row in cursor:
        print(f'''
        userID: ........{row[0]}
        Name: ..........{row[1]}
        Age: ...........{row[2]}
        Condition: .....{row[3]}
        Medicine: ......{row[4]}
        Temprement: ....{row[5]}
        Adoptable: .....{row[6]}
        ''')
    cursor.close()
    conn.close()
except(Exception, mysql.connector.Error) as error:
    print('Error while fetching data from MySQL', error)