import mysql.connector

class Database:
    def __init__(self, hostname, username, password, database = None):
        self.DB = mysql.connector.connect(
            host = hostname,
            user = username,
            password = password,
            database = database
        )
        self.CURSOR = self.DB.cursor()
        print(f'Conexão com {hostname} realizada com sucesso!')
        
    def COMMIT(self):
        self.DB.commit()
        print('Commit realizado com sucesso!')
    
    def USE(self, query : str):
        self.CURSOR.execute(query)
    
    # DDL
    def CREATE(self, query : str):
        self.CURSOR.execute(query)
        print(f'{'DATABASE' if 'DATABASE' in query else 'TABLE'} criado(a) com sucesso!') # O PRINT SÓ ESTÁ CONFIGURADO PARA RECEBER DATABASE OU TABLE
        self.COMMIT()
    
    def ALTER(self, query : str):
        self.CURSOR.execute(query)
        print(f'{'DATABASE' if 'DATABASE' in query else 'TABLE'} criado(a) com sucesso!') # O PRINT SÓ ESTÁ CONFIGURADO PARA RECEBER DATABASE OU TABLE
        self.COMMIT()
    
    def DROP(self, query : str):
        self.CURSOR.execute(query)
        print(f'{'DATABASE' if 'DATABASE' in query else 'TABLE'} criado(a) com sucesso!') # O PRINT SÓ ESTÁ CONFIGURADO PARA RECEBER DATABASE OU TABLE
        self.COMMIT()
    
    def TRUNCATE(self, query : str):
        self.CURSOR.execute(query)
        print(f'Os registros da TABLE foram limpados com sucesso!')
        self.COMMIT()
    
    # DQL
    def SELECT(self, query : str):
        self.CURSOR.execute(query)
        data_querys = self.CURSOR.fetchall()
        print('Consulta realizado com sucesso!')
        return data_querys
    
    # DML
    def INSERT(self, query : str):
        self.CURSOR.execute(query)
        self.COMMIT()
        print('Dados inseridos com sucesso!')
    
    def UPDATE(self, query : str):
        self.CURSOR.execute(query)
        self.COMMIT()
        print('Atualização de dados da tabela realizada com sucesso!')
    
    def DELETE(self, query : str):
        self.CURSOR.execute(query)
        self.COMMIT()
        print('Deleção completa com sucesso!')
    
    def close_cursor(self):
        self.CURSOR.close()
        print('Cursor encerrado com sucesso!')
    
    def close_connection(self):
        self.DB.close()
        print('Conexão encerrada com sucesso!')