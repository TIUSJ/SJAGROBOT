import requests
import time
import json

permisions =[215323461,818780128,-368194966,705268518,1008267781,746014353,-490653384,-499451163,1020918383,1334109159,1166641089]
permisionsCOI =[215323461,818780128,-368194966,705268518,-302990246,1008267781,746014353,-490653384, -499451163,1020918383, 1020918383, 1334109159,1166641089]


def Iniciar(self):
    print('teste')
    update_id = None
    while True:
        atualizacao = self.obter_mensagens(update_id)
        mensagens = atualizacao['result']
        if mensagens:
            for mensagem in mensagens:
                update_id = mensagem['update_id']
                chat_id = mensagem['message']['from']['id']
                resposta = self.criar_resposta()
                self.responder(resposta, chat_id)


def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout =100'
    if update_id:
        link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)


def criar_resposta(self):
    return 'Olá Bem vindo!'


def responder(self, resposta, chat_id):
    link_de_envio = f'{self.url_base}sendMessage?chat_id{chat_id}&text = {resposta}'
    requests.get(link_de_envio)
