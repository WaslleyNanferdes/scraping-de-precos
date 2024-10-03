from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector

def mysql_connect(host_name, user_name, user_password):
    db = None
    try:
        db = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
        )
        print('Conexão bem sucedida!')
    except ConnectionError as Error:
        print(f'Erro durante a conexão: {Error}')
    return db

def create_database(db, cursor, query):
    cursor.execute(query)
    db.commit()

# CRUD
def db_create(db, cursor, query):
    pass

def db_read(db, cursor, query):
    pass

def db_update(db, cursor, query):
    pass

def db_delete(db, cursor, query):
    pass

def main():
    host = ''
    user = ''
    pwd = ''
    query_create_db = '''CREATE DATABASE IF NOT EXISTS Produtos'''
    
    db = mysql_connect(host, user, pwd)
    cursor = db.cursor()
    create_database(db, cursor, query_create_db)
    print(db)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()