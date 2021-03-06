from telegram.ext import Updater, CommandHandler
import functions

#permisions =[215323461,818780128,-368194966,705268518,1008267781,746014353,-490653384,-499451163,1020918383,1334109159,1166641089]
#permisionsCOI =[215323461,818780128,-368194966,705268518,-302990246,1008267781,746014353,-490653384, -499451163,1020918383, 1020918383, 1334109159,1166641089]


##Functions

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


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




