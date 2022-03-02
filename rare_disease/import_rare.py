import pandas as pd 
import os
from mysql.connector import connect, Error
from dotenv import dotenv_values


config = dotenv_values('connect.env')
rare_diseases = pd.read_csv('rare_diseases.csv')

create_database_query = """
CREATE DATABASE IF NOT EXISTS rare_disease
"""
create_table_query = """
CREATE TABLE IF NOT EXISTS disease_gene_protein(
    disease_gene_protein_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    disease_name VARCHAR(255) NOT NULL,
    gene_name VARCHAR(255) NOT NULL,
    protein_name VARCHAR(255) NOT NULL
)
"""

for i,row in rare_diseases.iterrows():
    try:
        with connect(
            host="localhost", 
            user = config['user'], 
            password = config['password'],
            database = "rare_disease"
            ) as db:
            with db.cursor() as cursor:
                sql_query = """
                 INSERT INTO disease_gene_protein (disease_name, gene_name, protein_name)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(sql_query, tuple(row))
                print("Data inserted successfully")
                db.commit()
    except Error as err:
        print(err)
