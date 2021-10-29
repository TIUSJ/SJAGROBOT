
class Permission():

    def __init__(self):
        self.pDefault = [215323461,818780128,-368194966,705268518,1008267781,746014353,-490653384,-499451163,1020918383,1334109159,1166641089]
        self.pCOI = [215323461, 818780128, -368194966, 705268518, -302990246, 1008267781, 746014353, -490653384,
                     -499451163, 1020918383, 1020918383, 1334109159,1166641089]

    def getPermission(self, p):
        if(p == 'd'):
            return self.pDefault
        else:
            return self.pCOI
