import database
import amazon_automation
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    host = ''
    user = ''
    pwd = ''
    database_name = 'scraping_vendas'
    query_create_db = f'''CREATE DATABASE IF NOT EXISTS {database_name};'''
    query_create_table = '''CREATE TABLE IF NOT EXISTS produtos(
        nome_produto VARCHAR(255) NOT NULL,
        preco_produto DOUBLE NOT NULL,
        vendedor_produto VARCHAR(255) NOT NULL,
        reembolso_produto VARCHAR(255) NOT NULL,
        link_produto VARCHAR(600) NOT NULL,
        data_coleta DATE,
        data_entrega_produto DATE,
        data_entrega_rapida_produto DATE,
        disponobilidade_produto BOOLEAN NOT NULL DEFAULT FALSE,
        avaliacao_produto DOUBLE,
        PRIMARY KEY(data_coleta),
        UNIQUE(link_produto),
        CHECK(preco_produto > 0)
    );'''
    query_use_db = f'USE {database_name}'
    
    # Conexão com banco de dados
    DB = database.Database(host, user, pwd)
    DB.CREATE(query_create_db)
    DB.USE(query_use_db)
    DB.CREATE(query_create_table)
    
    # Encerramento da conexão
    DB.close_cursor()
    DB.close_connection()

if __name__ == "__main__":
    main()