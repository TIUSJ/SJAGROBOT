'''
Classe:     Permission
Objetivo:   Controlar permissões de retorno dos relatórios
Autor:      Alisson Cavalcanti Galvão
Data:       08/11/2021
'''


class Permission():

    def __init__(self):
        self.pDefault = [215323461,818780128,-368194966,705268518,1008267781,746014353,-490653384,-499451163,1020918383,1334109159,1166641089]
        self.pCOI = [215323461, 818780128, -368194966, 705268518, -302990246, 1008267781, 746014353, -490653384, -499451163, 1020918383, 1020918383, 1334109159]


    def getPermission(self, p):
        if(p == 'd'):
            print('DefaultPermission')
            #print(self.pDefault)
            return self.pDefault
        elif(p == 'c'):
            print('COIPermission')
            #print(self.pCOI)
            return self.pCOI


