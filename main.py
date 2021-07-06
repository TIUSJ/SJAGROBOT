import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import cx_Oracle
import pandas as pd


df = pd.DataFrame({"QTD_CANA":[],
                   "QTD_CANA_ANL":[],
                  "KG_BRIX":[],
                   "KG_PEX":[],
                   "KG_FIBRA":[],
                   "KG_PUB":[]})

dsn_tns = cx_Oracle.makedsn('usaojose10.grupocavalcanti.intranet',  1521, service_name='TESTECTL')
conn = cx_Oracle.connect(user=r'PIMSCS', password='USJPIMS1', dsn=dsn_tns)

c = conn.cursor()

bot = telepot.Bot("1143523201:AAGfUzLGrx8se3g97cMLo-k-eBGEFpLORGE")
bot.\
    permisions =[215323461,818780128,746014353,-490653384,-499451163,1020918383]

def getRel(data):
  conn = cx_Oracle.connect(user=r'PIMSCS', password='USJPIMS1', dsn=dsn_tns)

  c = conn.cursor()
  querystring = "select * from HISTQUEIMA_21718 where DT_HISTORICO ='%s'"%(data)
  c.execute(querystring)
  index = 0
  for row in c:

    df.loc[index] = [row[5],row[6],row[9],row[10],row[11],row[30]]
    index+=1

  x = df.sum(axis = 0, skipna = True)
  x = x.to_dict()
  conn.close()
  return (x)

def getAllMsg(msg):

    id = msg['chat']['id']
    fName = msg['chat']['first_name']
    texts = msg['text']
    print(id)
    print(fName)
    print(texts)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Relatório Ordens de Corte", callback_data='press')],
    ])
    if id in permisions:

        texts = texts.upper()
        texts = texts.split(" ")
        if texts[0] == "RL":
            dados = getRel(texts[1])
            bot.sendMessage(id,"Relatório do dia "+texts[1]+".\nQuantidade de cana (entrada): %s\nQuantidade de cana (analizada): %s\nBRIX: %s\nPEX: %s\nFIBRA: %s\nPBU: %s"%(dados['QTD_CANA'], dados['QTD_CANA_ANL'], round(dados['KG_BRIX']), round(dados['KG_PEX']), round(dados['KG_FIBRA']), round(dados['KG_PUB'])))
        else:
            bot.sendMessage(msg['chat']['id'], 'Olá '+msg['chat']['first_name'] +"! Seja Bem Vindo a versão alpha do ChatBot da SJAgro! "+ "Favor informar alguma data da safra(17-18) que foi do dia 27 de Agosto de 2017 até 18 de Janeiro de 2018. "
                                                                                   "Para obter o relatório enviar 'RL  DIA/MES/ANO!'")

    else:
        bot.sendMessage(msg['chat']['id'], 'Olá ' + msg['chat']['first_name'] + '! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')
def callbackM(msg):

    id, from_id,query_data = telepot.glance(msg, flavor='callback_query')

    bot.answerCallbackQuery(id,text="Relatório tal")


bot.message_loop({'chat': getAllMsg,
                  'callback_query': callbackM})
while True:
    pass