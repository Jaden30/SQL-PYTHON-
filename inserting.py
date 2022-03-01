from getpass import getpass
from mysql.connector import connect, Error


first_name = input("Please enter Cam and Mitchell son's name: ")
last_name = input("Please enter Cam and Mitchell son's last name: ")

insert_individual_query = """
INSERT INTO Individual
(first_name, last_name)
values ( %s, %s )
"""
family = [
  (first_name, last_name)
]

try: 
    print("Connecting to MySQL database...\n")
    with connect(
        host = "localhost",
        user = input("Please enter your username: "),
        passwd = getpass("Enter password: "),
        database = "modern_family"
    ) as db:
        print("Connected to database")
        with db.cursor() as cursor:
            cursor.executemany(insert_individual_query, family)
            db.commit()
            print("Record inserted successfully into Individual table")
except Error as err:
    print(err)