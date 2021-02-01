import mysql.connector
from mysql.connector import connect, Error, MySQLConnection
import colorama
from colorama import Fore, Style
colorama.init()

conn = connect(
        host='127.0.0.1',
        user='admin',
        password='Phipsy1!',
        database='practice'
)

try:
    cursor = conn.cursor()
    cursor.execute('select * from cats')
    #cursor = conn.cursor(buffered=True) <-- this was an attempt at getting python to not be lazy and to show me all of the data entries. it belongs at the end of line 15.
    
    row = ('ID', 'Name', 'Age', 'Condition', 'Medecine', 'Temperament', 'Adoptable')
    for row in cursor:
        print(f'''
        ID: .......... {Fore.RED + str(row[0]) + Style.RESET_ALL}
        Name: ........ {Fore.BLUE + row[1] + Style.RESET_ALL}
        Age: ......... {Fore.BLUE + str(row[2]) + Style.RESET_ALL}
        Condition: ... {Fore.BLUE + row[3] + Style.RESET_ALL}
        Medicine: .... {Fore.BLUE + row[4] + Style.RESET_ALL}
        Temperament: . {Fore.BLUE + row[5] + Style.RESET_ALL}
        Adoptable: ... {Fore.BLUE + row[6] + Style.RESET_ALL}
        ''')

    cursor.close()
    conn.close()
except(Exception, mysql.connector.Error) as error:
    print('Error while fetching data from MySQL', error)