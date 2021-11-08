#from oracle import *
#from datetime import datetime, date, timedelta
#import matplotlib.pyplot as plt

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import functions
import TelegramBot


##HANDLERS

def main():
    #updater = Updater('878172789:AAFgF98c8ENq1e17PvfRB_no5uI4dUyv8_I', use_context=False)
    updater = Updater('1143523201:AAGfUzLGrx8se3g97cMLo-k-eBGEFpLORGE')

    dp = updater.dispatcher

    #15 funções

    #1
    dp.add_handler(
        CommandHandler('relatorio', functions.relatorioEntradaDia)
    )

    #2
    dp.add_handler(
        CommandHandler('relatoriodiaanterior', functions.relatorioEntradaDiaAnterior)
    )

    #3
    dp.add_handler(
        CommandHandler('relatoriogeral', functions.relatorioGeralDiaAnterior)
    )

    #4
    dp.add_handler(
        CommandHandler('relatoriodensidade', functions.relatorioEntradaDensidade)
    )

    #5
    dp.add_handler(
        CommandHandler('relatorioprecipitacao', functions.relatorioGeralDiaAnteriorPress)
    )

    #6
    dp.add_handler(
        CommandHandler('boletim', functions.relatorioBoletim)
    )

    #7
    dp.add_handler(
        CommandHandler('relatoriofrente1', functions.relatorioFREN1)
    )

    #8
    dp.add_handler(
        CommandHandler('relatoriofrente2', functions.relatorioFREN2)
    )

    #9
    dp.add_handler(
        CommandHandler('relatoriofrente3', functions.relatorioFREN3)
    )

    #10
    dp.add_handler(
        CommandHandler('relatoriofrente5', functions.relatorioFREN5)
    )

    #11
    dp.add_handler(
        CommandHandler('graficofrentes', functions.graficoEntrFren)
    )

    #12
    dp.add_handler(
        CommandHandler('graficotcsetedias', functions.graficoLast7Days)
    )

    #13
    dp.add_handler(
        CommandHandler('relatorioostipo', functions.relatorioOSTipo)
    )

    #14
    dp.add_handler(
        CommandHandler('disponibilidade', functions.getDisponibilidade)
    )

    #15
    dp.add_handler(
      CommandHandler('consultasaldoped', functions.consultaSaldo)
    )

    #16
    #dp.add_handler(CommandHandler('IT', functions.it))



    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




