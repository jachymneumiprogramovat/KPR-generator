idlist = ["a","b","c","d","e","f","g","h","i","j","k"]

body = []
primky=[]

class primka:
    def __init__(self,elements:list[bod]) -> None:
        self.elements=elements
        self.protina = []
    
    def update_protina(self)->None:
        for primka in primky:
            for element in self.elements:
                if element in primka.elements:
                    self.protina.append(primka)


class bod:
    def __init__(self,protina:list[primka],id:str) -> None:
        self.id=id
        self.nalezi=protina
        self.navlne = []
    
    def update_navlne(self)->None:
        for bod in body:
            for primka in bod.protina:
                if primka in self.nalezi:
                    self.navlne.append(bod)


def protahni_primku(primka:primka,bod:bod)->None:
    primka.elements.append(bod)
    bod.nalezi.append(primka)

def pridej_primku(body:list[bod])->primka:
    nprimka= primka(body)
    primky.append(nprimka)
    for bod in body:
        bod.nalezi.append(nprimka)
    return nprimka

def pridej_bod(primka1:primka,primka2:primka)->bod:
    nbod = bod([primka1,primka2],idlist[len(body)])
    body.append(nbod)


#delete later meaby useles
def disjunkt_primky(primka1:primka,primka2:primka)->bool:
    for element in primka1.elements:
        if element in primka2.elements:
            return False
    return True


#first the primka axiom

