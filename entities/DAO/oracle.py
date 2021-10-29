import pandas as pd
from entities.model.connect import Connect

global c
cs = Connect()
c = cs.returnC()


def getRel(data):

  querystring = "select CD_FREN_TRAN, SUM(QT_LIQUIDO) from APT_CARGAS where DT_ENTRADA like '%s' GROUP BY CD_FREN_TRAN ORDER BY CD_FREN_TRAN"%(data)
  c.execute(querystring)

  dic ={}
  for row in c:
    if row[1] == None:
        dic[row[0]]= 0
    else:
        dic[row[0]] = row[1]

  #c.close()

  return (dic)

def getRelGeral(data):

  querystring = x = "select SUM(QT_CANA_ENT),SUM(QT_CARGA_ENT),SUM(QT_CANA_ANL),SUM(VL_PZA),SUM(VL_PCC),SUM(VL_AGIO),SUM(VL_ATR) from PIMSCS.HISTUPNV1 where DT_REF like '%s' GROUP BY DT_REF"%(data)
  c.execute(querystring)
  dic ={}
  for row in c:

    dic['Total cana entregue'] = str((row[0])/1000) +" ton"
    dic['Total cargas entregue'] = (row[1])
    dic['Total cana analizada'] = str((row[2])/1000) + " ton"
    dic['Valor Pureza'] = (row[3])
    dic['Valor PC'] = (row[4])
    dic['Valor ágio'] =(row[5])
    dic['Valor ATR'] = (row[3])
    a = (100*row[2])/row[0]
    dic['Porcentagem de cana analisada'] = "%.2f" % a + "%"


  #c.close()

  return (dic)

def getRelDensidade(data):

  querystring = "select CD_FREN_TRAN, AVG(QT_LIQUIDO) from APT_CARGAS where DT_ENTRADA like '%s' GROUP BY CD_FREN_TRAN ORDER BY CD_FREN_TRAN"%(data)
  c.execute(querystring)

  dic ={}
  for row in c:

    dic[row[0]]= row[1]

  #c.close()


  return (dic)

def getRelDensidadeTotal(data):

  querystring = "select  AVG(QT_LIQUIDO) from APT_CARGAS where DT_ENTRADA like '%s' GROUP BY DT_ENTRADA"%(data)
  c.execute(querystring)

  for row in c:
    resultado = row[0]
  #c.close()

  return (resultado)

def getRelTMP(data):

  querystring = "select CD_FREN_TRAN,AVG(QT_HRQUEIMDES) from APT_CARGAS where DT_ENTRADA like '%s' and FG_CANA_CRUA = 'N' GROUP BY CD_FREN_TRAN"%(data)
  c.execute(querystring)
  dic ={}

  for row in c:

    dic[row[0]]= row[1]

  #c.close()

  return (dic)

def getRelImpur(data):

  querystring = "select CD_FREN_TRAN,AVG(QT_IMPUR_TERRA), AVG(QT_IMPUR_VEG) from APT_CARGAS where DT_ENTRADA like '%s' GROUP BY CD_FREN_TRAN"%(data)
  c.execute(querystring)
  dic ={}

  for row in c:

    if row[1]==None:
      mineral = 0
    else:
      mineral = row[1]
    if row[2]==None:
      vegetal = 0
    else:
      vegetal = row[2]

    dic[row[0]]= {'Mineral': mineral, 'Vegetal': vegetal}

  #c.close()


  return (dic)

def getATR(data):

    querystring = '''select CD_FREN_TRAN as FRENTE,
                            ROUND(AVG(QT_PCC),2) as POLCANA,
                            ROUND(AVG(QT_PEX),2) as POLCALDO,
                            ROUND(AVG(QT_ARCALDO),2) as AR,
                            ROUND(AVG(QT_FIBRA),2) as FIBRA,
                            ROUND(AVG(QT_PZA),2) AS PUREZA,
                            ROUND(AVG(QT_BRIX),2)AS BRIX,
                            ROUND(AVG((QT_PCC*9.36814)+((QT_ARCALDO*(1-(0.01*QT_FIBRA)*QT_FATORC))*8.9)),2)AS ATR 
                    from APT_CARGAS 
                    where DT_ENTRADA like '%s' and FG_ANALISE='S' 
                    group by CD_FREN_TRAN order by FRENTE''' % (data)
    c.execute(querystring)

    dic = {}
    for row in c:
        dic[row[0]] = {"POLCANA":row[1],"POLCALDO":row[2],"AR": row[3],"FIBRA":row[4],"PUREZA": row[5],"BRIX": row[6],"ATR":row[7]}

    #c.close()

    return (dic)

def getTC(data):

    querystring = "select SUM(QT_LIQUIDO/1000) from  APT_CARGAS where DT_ENTRADA like '%s' UNION select SUM(QT_LIQUIDO/1000) from APT_CARGAS where DT_ENTRADA like '%s'  and FG_ANALISE='S'" % (data,data)
    #querystring = "select SUM(QT_LIQUIDO / 1000) from APT_CARGAS UNION select SUM(QT_LIQUIDO / 1000) from APT_CARGAS where FG_ANALISE = 'S'"
    c.execute(querystring)
    dic = {}

    x = "TC Analisada"
    for row in c:
        dic[x] = row[0]
        x = "TC Entregue"
    #c.close()
    y = (100*dic['TC Analisada'])/dic["TC Entregue"]
    dic['Porcentagem de TC analisada'] = "%.2f" % y + "%"
    return (dic)

def getCargasTotal(data):

    querystring = "select count(*) from APT_CARGAS where DT_ENTRADA like '%s'" % (data)
    c.execute(querystring)

    dic = {}
    x = "Total de cargas entregues"
    for row in c:
        dic[x] = row[0]
    #c.close()

    return (dic)

def getRelPres(data):

  querystring = "SELECT POSTOMETEO.DE_POSTO, CLIMAT.QT_LEITURA FROM CLIMAT JOIN POSTOMETEO ON CLIMAT.CD_POSTO = POSTOMETEO.CD_POSTO WHERE DT_OPERACAO like'%s'"%(data)
  c.execute(querystring)
  dic ={}

  for row in c:

    dic[row[0]]= row[1]

  #c.close()

  return (dic)

def getRelBoletim(data):

  querystring = '''SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = 'CANPROPRIA' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = '0CANFORNEC' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = '0CANAMOIDA' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = '0CANA_DISP' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = '0000PROCAC' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = '0DESMREFKG' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = 'ENERGVENDI' AND LAN_HORA = 'XXXX'
              UNION
              SELECT VAR_CODIGO,LAN_VALOR FROM PROLANCA WHERE LAN_DATA = '%s' AND VAR_CODIGO = 'PRODTOTHID' AND LAN_HORA = 'XXXX'''% (data, data, data, data, data, data, data, data)+"'"
  c.execute(querystring)
  dicConvert = {'CANPROPRIA': 'Cana propria(TON)',
                '0CANFORNEC': 'Cana fornecedor(TON)',
                '0CANAMOIDA': 'Cana moida(TON)',
                '0CANA_DISP': 'Cana disponivel(TON)',
                '0000PROCAC': 'Refinado 50 kg(sc)',
                '0DESMREFKG': 'Produção de açúcar refinado(KG)',
                'ENERGVENDI': 'Energia vendida em KWH ',
                'PRODTOTHID': 'Produção de alcool hidratado(LT)'}

  dic ={}
  for row in c:
    if row[1] == None:
        dic[dicConvert[row[0]]]= 0
    else:
        dic[dicConvert[row[0]]] = row[1]

  #c.close()

  return (dic)

def getRelByFren(data, frente):

  querystring ='''select DA_UPNIVEL1, QT, ATR, TMP  from 
                (select CD_UPNIVEL1, SUM(QT_LIQUIDO/1000) as QT,  ROUND(AVG((QT_PCC*9.36814)+((QT_ARCALDO*(1-(0.01*QT_FIBRA)*QT_FATORC))*8.9)),2)AS ATR, ROUND(AVG(QT_LIQUIDO/1000)) as TMP from APT_CARGAS where DT_ENTRADA like '%s' and CD_FREN_TRAN = %s GROUP BY CD_UPNIVEL1 ORDER BY CD_UPNIVEL1)x
                inner join 
                (select CD_UPNIVEL1, DA_UPNIVEL1 from UPNIVEL1)y 
                on x.CD_UPNIVEL1=y.CD_UPNIVEL1'''%(data, frente)
  c.execute(querystring)
  dic ={}

  for row in c:
    if row[1] == None:
        dic[row[0]]= 0
    else:
        dic[row[0]] = [row[1], row[2], row[3]]

  #c.close()

  return (dic)

def getOSRel(data):

  querystring ='''select  descr,ossum,descricao from
                (select empresa,ossum,descricao from
                (select codiempr as empresa, codipoma as tipo, count(*) as OSSUM from OSRESUM where DATAENTRA = '%s' group by codiempr,codipoma)x left join
                (select codiespe,descricao from especie)y
                on x.tipo = y.codiespe)z left join
                (select codiempr,descr from empresa)w
                on z.empresa = w.codiempr'''%(data)
  c.execute(querystring)
  dic ={}

  for row in c:

    dic[row[0]]= [row[2],row[1]]

  #c.close()

  return (dic)


def getClasses(equipamento):

  querystring ='''SELECT X.CODIEMPR,X.NUMEEQUI,X.CODIRELAC3,DESCRELAC3.DESCRICAO FROM
                (SELECT CODIEMPR,NUMEEQUI,CODIRELAC3 FROM(
                SELECT EQPTORELAC3.CODIEMPR, EQPTORELAC3.NUMEEQUI,EQPTORELAC3.DATA, EQPTORELAC3.HORA,EQPTORELAC3.CODIRELAC3 
                FROM EQUIPAMENTO
                INNER JOIN EQPTORELAC3
                ON EQUIPAMENTO.NUMEEQUI = EQPTORELAC3.NUMEEQUI 
                AND EQUIPAMENTO.CODIEMPR = EQPTORELAC3.CODIEMPR
                ORDER BY  DATA DESC , HORA DESC)
                WHERE NUMEEQUI = '%s'
                AND ROWNUM = 1)X
                INNER JOIN DESCRELAC3
                ON DESCRELAC3.CODIRELAC3 = X.CODIRELAC3'''%(equipamento)
  c.execute(querystring)

  dic = {}

  var = 'CODC2'
  var1 = 'DESC2'

  for row in c:

    dic['EQUIPAMENTO']= row[1]
    dic[var]=row[2]
    dic[var1]= row[3]
    dic['DISPONIBILIDADE'] = 'SIM'



  #c.close()

  return (dic)

def getEquipamentos():

  querystring ='''SELECT NUMEEQUI FROM EQUIPAMENTO WHERE CODIINES = 0 AND CODIEMPR = 6'''
  c.execute(querystring)
  lista = []

  for row in c:

    dic = getClasses(str(row[0]))
    if dic != {}:
        lista.append(dic)
  #c.close()

  dataframe = pd.DataFrame(lista)
  return (dataframe)

def getOSAbertas():

  querystring ="SELECT NUMEEQUI FROM OSRESUM WHERE DATASAIDA IS NULL AND MBFILLER01 = 'CON' AND CODIEMPR = 6 UNION SELECT NUMEEQUI FROM OSRESUM WHERE DATASAIDA IS NULL AND MBFILLER01 = '' AND CODIEMPR = 6"
  c.execute(querystring)
  lista = []

  for row in c:
    lista.append(row[0])
  #c.close()
  return (lista)


def getSolicitacao(data,depto):
    print("teste1 - oRACLE", (data),(depto));
    print("teste2 - oRACLE", Connect.self.dsn_tns);
    print("teste3");
   # querystring = "SELECT POSTOMETEO.DE_POSTO, CLIMAT.QT_LEITURA FROM CLIMAT JOIN POSTOMETEO ON CLIMAT.CD_POSTO = POSTOMETEO.CD_POSTO WHERE DT_OPERACAO like'%s'" % (data)
    #querystring = "SELECT M.NUMEROMOV, M.STATUS FROM TMOV M, TITMMOV I WHERE M.CODCOLIGADA = I.CODCOLIGADA AND M.IDMOV = I.IDMOV AND M.CODTMV='1.1.03' AND I.CODDEPARTAMENTO = '842' AND M.STATUS = 'A' AND DATAEMISSAO like'%s'" % (data)
    querystring = "SELECT M.NUMEROMOV, M.STATUS, I.CODDEPARTAMENTO,P.CODIGOREDUZIDO,P.NOMEFANTASIA,S.SALDOFISICO2 FROM TMOV M JOIN TITMMOV I ON M.CODCOLIGADA = I.CODCOLIGADA AND M.IDMOV = I.IDMOV JOIN TPRODUTO P ON P.CODCOLPRD = I.CODCOLIGADA AND P.IDPRD = I.IDPRD JOIN TPRDLOC S ON S.IDPRD = P.IDPRD WHERE  M.CODTMV='1.1.03' AND M.STATUS = 'A' AND M.DATAEMISSAO <='%s' AND I.CODDEPARTAMENTO = '%s'"  % (data,depto)
    print(querystring);
    c.execute(querystring)
    print("teste4");
    dic = {}

    for row in c:
        dic[row[0]] = row[1],row[2],row[3],row[4],row[5]

    #c.close()

    return (dic)












