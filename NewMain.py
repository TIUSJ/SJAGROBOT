from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from oracle import *
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

permisions =[215323461,818780128,-368194966,705268518,1008267781,746014353,-490653384,-499451163,1020918383, 1334109159]
permisionsCOI =[215323461,818780128,-368194966,705268518,-302990246,1008267781,746014353,-490653384, -499451163,1020918383, 1020918383, 1334109159]


def relatorioEntradaDia(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    print(hoje)
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório de entrada toneladas por frente\n%s\n================\n'%(hoje)
        relatorioDia = getRel(hoje)
        relatorioDiaTMP = getRelTMP(hoje)
        relatorioDiaATR = getATR(hoje)


        print(relatorioDia)
        for key, value in relatorioDia.items():
            if value == None:
                value = 0

            key, value = round(key),value
            if key == 6:
                if key in relatorioDiaTMP.keys() and relatorioDiaTMP[key] != None:
                    msg += "Frente 6(Fornec)\nQt cana :%.2f ton\nTMP: %.2f \n"%(value/1000,relatorioDiaTMP[key])

                else:
                    msg += "Frente 6(Fornec)\nQt cana :%.2f ton\n" % (value / 1000)


                if key in relatorioDiaATR.keys() and relatorioDiaATR[key]['ATR'] != None:
                    msg+= "ATR : %.2f\n================\n"%(relatorioDiaATR[key]['ATR'])


                msg+="================\n"
            elif key == 99:
                if key in relatorioDiaTMP.keys()  and relatorioDiaTMP[key] != None:
                    msg += "Frente 99(Fornec)\nQt cana :%.2f ton\nTMP: %.2f \n"%(value/1000,relatorioDiaTMP[key])
                else:
                    msg += "Frente 99(Fornec)\nQt cana :%.2f ton\n" % (value / 1000)
                if key in relatorioDiaATR.keys() and relatorioDiaATR[key]['ATR'] != None:
                    msg+= "ATR : %.2f\n================\n"%(relatorioDiaATR[key]['ATR'])

                msg += "================\n"
            else:
                if key in relatorioDiaTMP.keys()  and relatorioDiaTMP[key] != None:
                    msg += "Frente %s \nQt cana :%.2f ton\nTMP: %.2f \n"%(key,value/1000, relatorioDiaTMP[key])
                else:
                    msg += "Frente %s \nQt cana :%.2f ton\n" % (key, value / 1000)
                if key in relatorioDiaATR.keys() and relatorioDiaATR[key]['ATR'] != None:
                    msg+= "ATR : %.2f\n================\n"%(relatorioDiaATR[key]['ATR'])


                msg += "================\n"


            total += value/1000
        msg+= "Total TC : %s ton"%(round(total))


        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioEntradaDiaAnterior(bot, update):
        chat_id = update.message.chat_id
        print(chat_id)
        #now = datetime.now()
        #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #dt_string = dt_string.split(" ")
        ontem = date.today() - timedelta(days=1)
        ontem = ontem.strftime('%d/%m/%Y')
        print(ontem)
        total = 0
        if chat_id in permisionsCOI:

            msg = 'Relatório de entrada toneladas por frente\n%s\n================\n' % (ontem)
            relatorioDia = getRel(ontem)
            relatorioDiaTMP = getRelTMP(ontem)
            relatorioDiaATR = getATR(ontem)

            print(relatorioDia)
            for key, value in relatorioDia.items():
                if value == None:
                    value = 0

                key, value = round(key), value
                if key == 6:
                    if key in relatorioDiaTMP.keys() and relatorioDiaTMP[key] != None:
                        msg += "Frente 6(Fornec)\nQt cana :%.2f ton\nTMP: %.2f \n" % (
                        value / 1000, relatorioDiaTMP[key])

                    else:
                        msg += "Frente 6(Fornec)\nQt cana :%.2f ton\n" % (value / 1000)

                    if key in relatorioDiaATR.keys() and relatorioDiaATR[key]['ATR'] != None:
                        msg += "ATR : %.2f\n================\n" % (relatorioDiaATR[key]['ATR'])

                    msg += "================\n"
                elif key == 99:
                    if key in relatorioDiaTMP.keys() and relatorioDiaTMP[key] != None:
                        msg += "Frente 99(Fornec)\nQt cana :%.2f ton\nTMP: %.2f \n" % (
                        value / 1000, relatorioDiaTMP[key])
                    else:
                        msg += "Frente 99(Fornec)\nQt cana :%.2f ton\n" % (value / 1000)
                    if key in relatorioDiaATR.keys() and relatorioDiaATR[key]['ATR'] != None:
                        msg += "ATR : %.2f\n================\n" % (relatorioDiaATR[key]['ATR'])

                    msg += "================\n"
                else:
                    if key in relatorioDiaTMP.keys() and relatorioDiaTMP[key] != None:
                        msg += "Frente %s \nQt cana :%.2f ton\nTMP: %.2f \n" % (key, value / 1000, relatorioDiaTMP[key])
                    else:
                        msg += "Frente %s \nQt cana :%.2f ton\n" % (key, value / 1000)
                    if key in relatorioDiaATR.keys() and relatorioDiaATR[key]['ATR'] != None:
                        msg += "ATR : %.2f\n================\n" % (relatorioDiaATR[key]['ATR'])

                    msg += "================\n"

                total += value / 1000
            msg += "Total TC : %s ton" % (round(total))

            bot.send_message(chat_id=chat_id, text=msg)

        else:
            bot.send_message(chat_id=chat_id,
                             text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioGeralDiaAnterior(bot, update):
    chat_id = update.message.chat_id
    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.strftime('%d/%m/%Y')
    if chat_id in permisionsCOI:
        msg = 'Relatório de entrada geral\n%s\n================\n' % (yesterday)
        relatorioDia = getTC(yesterday)
        relatorioDiaATR = getATR(yesterday)
        relatorioDiaCargaTotal = getCargasTotal(yesterday)
        relatorioDiaAntTMP = getRelTMP(yesterday)
       # relatorioDiaTESTE = getTESTE(yesterday)
        print(relatorioDia)
        for key, value in relatorioDia.items():
            msg+='%s : %s\n================\n'%(key,value)

        ''' for key, value in relatorioDiaTESTE.items():
                msg += '%s : %s\n================\n' % (key, value)'''

        for key, value in relatorioDiaCargaTotal.items():
            msg+='%s : %s\n================\n'%(key,value)
        for key,value in relatorioDiaATR.items():
            msg+="Frente %s\n\nPOLCANA : %.2f\nAR : %.2f\nFIBRA : %.2f\nPUREZA : %.2f\nBRIX : %.2f\nATR : %.2f\n"%(key,value['POLCANA'],value['AR'],value['FIBRA'],value['PUREZA'],value['BRIX'],value['ATR'])
            if key in relatorioDiaAntTMP.keys():
                msg+="TMP: %.2f\n"%(relatorioDiaAntTMP[key])
            msg+= '================\n'
        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioEntradaDensidade(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    print(hoje)
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório densidade de carga por frente\n%s\n================\n'%(hoje)
        relatorioDia = getRelDensidade(hoje)

        print(relatorioDia)
        for key, value in relatorioDia.items():
            if value == None:
                value = 0
            key, value = round(key), round(value)
            if key == 6:
                msg += "Frente 6(Fornec): %.2f ton\n================\n"%(value/1000)
            elif key == 99:
                msg += "Frente 99(Fornec): %.2f ton\n================\n"%(value/1000)

            else:
                msg += "Frente %s: %.2f ton\n================\n"%(key,value/1000)

            total += value/1000
        msg += "Total: %.2f ton"%(getRelDensidadeTotal(hoje)/1000)

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioGeralDiaAnteriorPress(bot, update):
    chat_id = update.message.chat_id
    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.strftime('%d/%m/%Y')
    if chat_id in permisions:
        msg = 'Relatório de Precipitação pluviometrica\n%s\n================\n' % (yesterday)
        relatorioDia = getRelPres(yesterday)
        for key, value in relatorioDia.items():
            msg+='%s : %s\n================\n'%(key,value)
        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioBoletim(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.strftime('%d/%m/%Y')
    print(yesterday)
    total = 0
    if chat_id in permisions:

        msg ='Boletim de Produção\n%s\n================\n'%(yesterday)
        relatorioBoletim = getRelBoletim(yesterday)

        print(relatorioBoletim)
        for key, value in relatorioBoletim.items():

            msg += "%s: %.2f\n================\n"%(key, value)

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioFREN1(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório de entrada de cana por Fazenda\n%s\nFrente 1\n================\n'%(hoje)
        relatorioBoletim = getRelByFren(hoje,1)

        print(relatorioBoletim)
        for key, value in relatorioBoletim.items():

            msg += "%s: %.2f\nATR: %s\nDensidade: %s\n================\n"%(key, value[0], value[1], value[2])

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioFREN2(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório de entrada de cana por Fazenda\n%s\nFrente 2\n================\n'%(hoje)
        relatorioBoletim = getRelByFren(hoje,2)

        print(relatorioBoletim)
        for key, value in relatorioBoletim.items():

           msg += "%s: %.2f\nATR: %s\nDensidade: %s\n================\n"%(key, value[0], value[1], value[2])

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioFREN3(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório de entrada de cana por Fazenda\n%s\nFrente 3\n================\n'%(hoje)
        relatorioBoletim = getRelByFren(hoje,3)

        print(relatorioBoletim)
        for key, value in relatorioBoletim.items():

           msg += "%s: %.2f\nATR: %s\nDensidade: %s\n================\n"%(key, value[0], value[1], value[2])

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def relatorioFREN5(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório de entrada de cana por Fazenda\n%s\nFrente 5\n================\n'%(hoje)
        relatorioBoletim = getRelByFren(hoje,5)

        print(relatorioBoletim)
        for key, value in relatorioBoletim.items():

           msg += "%s: %.2f\nATR: %s\nDensidade: %s\n================\n"%(key, value[0], value[1], value[2])

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def graficoEntrFren(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    print(hoje)
    total = 0
    if chat_id in permisionsCOI:

        #msg = 'Relatório de entrada toneladas por frente\n%s\n================\n' % (hoje)
        relatorioDia = getRel(hoje)
        total = 0
        labels = []
        sizes =[]
        for key, value in relatorioDia.items():
            labels.append("Frente %s"%(key))
            total+=value
            sizes.append(value)

        def percent(y):
            return ((100 * y) / total)

        sizes = list(map(percent, sizes))
        fig1, ax1 = plt.subplots()

       # ax1 = plt.subplots()
        plt.title("Porcentagem de entrada de cana por frente "+now.strftime("%d/%m/%Y %H:%M:%S"))
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.savefig('graficos/graficoFrente.png')

        bot.send_photo(chat_id=chat_id, photo=open('graficos/graficoFrente.png', 'rb'))
    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

def graficoLast7Days(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    print(hoje)
    total = 0
    if chat_id in permisionsCOI:
        def getLast7Days():
            daysList = []
            prodList = []
            for i in range(7, 0, -1):
                yesterday = date.today() - timedelta(days=i)
                yesterday = yesterday.strftime('%d/%m/%Y')
                d = getRel(yesterday)
                daysList.append(yesterday[0:5])
                prodList.append(sum(d.values()) / 1000)

            return (daysList, prodList)
        labels, produzido = getLast7Days()
        estimado = [9000, 9000, 9000, 9000, 9000, 9000, 9000]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, produzido, width, label='Produzido')
        rects2 = ax.bar(x + width / 2, estimado, width, label='Estimado')

        ax.set_ylabel('Produção')
        ax.set_title('Entrada diária TC. Estimado X Produzido')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend(loc=3, bbox_to_anchor=(0.75, 0))

        def autolabel(rects):

            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        plt.savefig('graficos/graficoSemanal.png')

        bot.send_photo(chat_id=chat_id, photo=open('graficos/graficoSemanal.png', 'rb'))
    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

'''SISMA'''

def relatorioOSTipo(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(" ")
    hoje = dt_string[0]
    total = 0
    if chat_id in permisionsCOI:

        msg ='Relatório Ordens de Serviços por Dia [SISMA]\n%s\n================\n'%(hoje)
        relatorioBoletim = getOSRel(hoje)

        print(relatorioBoletim)
        for key, value in relatorioBoletim.items():

            msg += "%s / %s: %s ordens abertas\n================\n"%(key, value[0],value[1])

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')


def getDisponibilidade(bot, update):
    chat_id = update.message.chat_id

    print(chat_id)

    if chat_id in permisionsCOI:

        msg = 'Processando...\nEm alguns instantes o gráfico de disponibilidade será enviado...'

        bot.send_message(chat_id=chat_id, text=msg)


        df = getEquipamentos()
        lista = getOSAbertas()
        print(lista)
        for i in lista:
            df.at[df.EQUIPAMENTO == i, 'DISPONIBILIDADE'] = 'NAO'

        df.groupby(['DESC2', 'DISPONIBILIDADE']).size().unstack().plot(kind='barh', stacked=True, figsize=(15,7))


        plt.savefig('graficos/graficoD.png')
        bot.send_photo(chat_id=chat_id, photo=open('graficos/graficoD.png', 'rb'))


    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')

'''RM'''
def consultaSaldo(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    if chat_id in permisionsCOI:

        msg = 'Posição das Solicitações\n%s\n================\n'
        solicitacao = getSolicitacao()

        print(solicitacao)
        for key, value in solicitacao.items():
           msg += "%s: %.2i\n================\n" % (key, value)

        bot.send_message(chat_id=chat_id, text=msg)

    else:
        bot.send_message(chat_id=chat_id,
                         text='Olá ! Desculpe mas você não tem permisao para acessar o bot :( Favor entrar em contato com o TI para o acesso')


def main():
    #updater = Updater('878172789:AAFgF98c8ENq1e17PvfRB_no5uI4dUyv8_I', use_context=False)
    updater = Updater('1143523201:AAGfUzLGrx8se3g97cMLo-k-eBGEFpLORGE')

    dp = updater.dispatcher

    dp.add_handler(
        CommandHandler('relatorio', relatorioEntradaDia)

    )

    dp.add_handler(
        CommandHandler('relatoriodiaanterior', relatorioEntradaDiaAnterior)

    )


    dp.add_handler(
        CommandHandler('relatoriogeral', relatorioGeralDiaAnterior)

    )

    dp.add_handler(
        CommandHandler('relatoriodensidade', relatorioEntradaDensidade)

    )
    dp.add_handler(
        CommandHandler('relatorioprecipitacao', relatorioGeralDiaAnteriorPress)

    )
    dp.add_handler(
        CommandHandler('boletim', relatorioBoletim)

    )
    dp.add_handler(
        CommandHandler('relatoriofrente1', relatorioFREN1)

    )
    dp.add_handler(
        CommandHandler('relatoriofrente2', relatorioFREN2)

    )
    dp.add_handler(
        CommandHandler('relatoriofrente3', relatorioFREN3)

    )
    dp.add_handler(
        CommandHandler('relatoriofrente5', relatorioFREN5)

    )
    dp.add_handler(
        CommandHandler('graficofrentes', graficoEntrFren)

    )
    dp.add_handler(
        CommandHandler('graficotcsetedias', graficoLast7Days)

    )
    dp.add_handler(
        CommandHandler('relatorioostipo', relatorioOSTipo)

    )

    dp.add_handler(
        CommandHandler('disponibilidade', getDisponibilidade)

    )

    dp.add_handler(
        CommandHandler('consultasaldoped', consultaSaldo)

    )


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
 



