import cx_Oracle


class Connect:
    global c;

    # método construtor
    def __init__(self):
        # conexão com banco de dados
        try:
            dsn_tns = cx_Oracle.makedsn('sja-hsdb03.grupocavalcanti.intranet', 1521, service_name='controle.usj.com.br')
            conn = cx_Oracle.connect(user='PIMSCS', password='USJPIMS1', dsn=dsn_tns)

            self.c = conn.cursor;

        except:
            print
            "Erro ao se conectar a base de dados!";

    # método destrutor
    def __del__(self):
        print
        "Conexão finalizada!";
        del self;
