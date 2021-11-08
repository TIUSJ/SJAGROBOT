'''
Classe:     Connect
Objetivo:   Iniciar e prover a conexão ao BD Oracle
Autor:      Alisson Cavalcanti Galvão
Data:       01/11/2021
'''


from decouple import config
import cx_Oracle

HOST = config('HOST')
PORT=config('PORT')
SN=config('SN')
USER=config('USER')
PASS=config('PASS')

#print(SN)

class Connect():

    def __init__(self):
        self.dsn_tns = cx_Oracle.makedsn(HOST, PORT, service_name=SN)
        self.conn = cx_Oracle.connect(user=USER, password=PASS, dsn=self.dsn_tns)
        self.c = self.conn.cursor()


    def returnC(self):
        return self.c
