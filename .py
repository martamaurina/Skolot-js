#Sākumskolas (tips – 1) skolotājs Bērziņš māca 15 stundas 2.a klasē.
#Vidusskolas (tips – 3) skolotājs Ozols māca šādus priekšmetus: matemātika un datorika, kopā 20 stundas.

class skolotajs:
    def __init__(self, stundas ):
        self.tips = None
        self.stundas = stundas
        
    #def izvade(self):
  #      pass


class sakskolotajs(skolotajs):
    def __init__(self,uzvards_s, klase, stundas):
        self.klase = klase
        self.uzvards_s = uzvards_s
        self.stundas = stundas
        self.tips = 1
    
    def izvade1(self):
        print (f"Sākumsskolas {self.tips} skolotājs {self.uzvards_s} māca {self.stundas} stundas {self.klase} klasē.")


class vidskolotajs(skolotajs):
    def __init__(self, prieksv, prieksd, uzvards_v, hv , hd, ):
        self.prieksv = prieksv
        self.prieksd = prieksd
        self.hd = hd
        self.hv = hv
        self.uzvards_v = uzvards_v
        self.tips = 3

    def kopa(self):
        return self.hv + self.hd

    def izvade2(self):
        print (f"Vidusskolas {self.tips} skolotājs {self.uzvards_v} māca šādus priekšmetus: {self.prieksv} un {self.prieksd}, kopā {self.kopa()} stundas.")


def sakums_skolotajs():
    uzvards_s = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    klase = input("Ievadiet skolotāja klasi: ")
    stundas = int(input("Ievadiet skolotaja stundu skaitu: "))
    skolotajs=sakskolotajs(uzvards_s, klase, stundas)
    skolotajs.izvade1()

def vidus_skolotajs():
    uzvards_v = input("Ievadiet visusskolas skolotāja uzvārdu: ")
    prieksv = input("Ievadiet pirmo pasniegto priekšmetu: ")
    hv = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    prieksd = input("Ievadiet otro pasniegto priekšmetu: ")
    hd = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    skolotajs=vidskolotajs(prieksv, prieksd, uzvards_v, hv, hd)
    skolotajs.izvade2()

sakums_skolotajs()
vidus_skolotajs()


