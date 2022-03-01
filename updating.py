from getpass import getpass
from mysql.connector import connect, Error

first_name = input("Please enter Cam and Mitchell new son's name: ")
last_name = input("Please enter Cam and Mitchell son's last name: ")


updating_sql_query = """
UPDATE Individual
SET first_name = "%s"
WHERE 
last_name = "%s"

SELECT individual_id 
FROM Individual 
WHERE first_name = "%s"

SELECT family_id
FROM Family
WHERE family_surname = "%s"

""" % (
    first_name, 
    last_name, 
    first_name, 
    last_name,
 )

try: 
    with connect(
        host = "localhost",
        user = input("Please enter your username: "),
        passwd = getpass("Enter password: "),
        database = "modern_family"
    ) as db:
        print("Connected to database")
        with db.cursor() as cursor:
            results = cursor.execute(updating_sql_query, multi=True)
            for result in results:
                if result.with_row:
                    print(result.fetchall())
except Error as err:
    print(err)