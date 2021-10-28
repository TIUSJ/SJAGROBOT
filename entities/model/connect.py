import cx_Oracle

class Connect():

    def __init__(self):
        self.dsn_tns = cx_Oracle.makedsn('sja-hsdb03.grupocavalcanti.intranet', 1521, service_name='controle.usj.com.br')
        self.conn = cx_Oracle.connect(user='PIMSCS1', password='PIMSCS1', dsn=self.dsn_tns)
        self.c = self.conn.cursor()


    def returnC(self):
        return self.c
