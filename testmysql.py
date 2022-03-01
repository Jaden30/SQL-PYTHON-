from getpass import getpass
from unittest import result
from mysql.connector import connect, Error 

""""
# using get pass module to hide the password input
# creating a database 
try:
    with connect(
        host="localhost",
        user=input("Please enter your username: "),
        passwd=getpass("Enter password: "),
    ) as db:
    # db is the database connection object 
        create_db_query = "CREATE DATABASE IF NOT EXISTS modern_family"
        with db.cursor() as cursor:
            cursor.execute(create_db_query)
            print("Database created")
except Error as err:
     print(err)
"""

""" how to connect to an existing database"""

create_individual_table_query = """
          CREATE TABLE IF NOT EXISTS Individual
          (
            individual_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL
          ) """
create_family_table_query = """
        CREATE TABLE IF NOT EXISTS Family(
            family_id INT AUTO_INCREMENT PRIMARY KEY,
            family_surname VARCHAR(255) NOT NULL
        ) """

create_family_members_table_query = """
        CREATE TABLE IF NOT EXISTS Family_Members(
            family_id INT NOT NULL,
            individual_id INT NOT NULL,
            FOREIGN KEY (family_id) REFERENCES Family(family_id) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (individual_id) REFERENCES Individual(individual_id) ON UPDATE CASCADE ON DELETE CASCADE,
            PRIMARY KEY (family_id, individual_id)
            
        )"""



"""
Create table in the database
The major thing is we are considering the fact that we are using a transactional engine to create the tables.
InnoDB supports foreign key constraints
Transactional engine are easy, it is easy to use rollback simple commands
try:
    with connect(
        host="localhost",
        user=input("Please enter your username: "),
        passwd = getpass("Enter password: "),
        database="modern_family"
    ) as db:
        print("Connected to database")
        with db.cursor() as cursor:
            cursor.execute(create_individual_table_query)
            cursor.execute(create_family_table_query)
            cursor.execute(create_family_members_table_query)
            db.commit()
            print("Tables created")
except Error as err:
    print(err)

"""

insert_individual_query = """
INSERT INTO Individual
(first_name, last_name)
VALUES ( %s, %s )
"""
individual = [
    ("Phil", "Dunphy"),
    ("Claire", "Dunphy"),
    ("Haley", "Dunphy"),
    ("Alex", "Dunphy"),
    ("Luke", "Dunphy"),
    ("Camerom", "Tucker"),
    ("Mitchell", "Pritchett"),
    ("Lily", "Tucker-Pritchett"),
    ("Jay", "Pritchett"),
    ("Gloria", "Delgado-Pritchett"),
    ("Manny", "Delgado"),
    ("Joe", "Pritchett"),
]

insert_family_query = """
INSERT INTO Family
( family_surname )
VALUE ( %s )
"""
family = [
    "Tucker-Pritchett",
    "Delgado-Pritchett",
]

insert_family_members_query = """
INSERT INTO Family_Members
(family_id, individual_id)
VALUES ( %s, %s )
"""
family_members = [
    (1,37),
    (1,38),
    (1,39),
    (1,40),
    (1,41),
    (2,42),
    (2,43),
    (2,44),
    (3,45),
    (3,46),
    (3,47),
    (3,48),
]

try:
    with connect(
        host="localhost",
        user=input("Please enter your username: "),
        passwd = getpass("Enter password: "),
        database="modern_family"
    ) as db:
        print("Connected to database")
        with db.cursor() as cursor:
            cursor.executemany(insert_family_members_query, family_members)
            db.commit()
            print("families inserted")
except Error as err:
    print(err)



