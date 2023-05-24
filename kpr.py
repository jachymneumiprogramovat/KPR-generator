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
    
    def satisfy_line_axiom(self)->None:
        for primka in primky:
            if primka in self.protina: continue
            for bod in primka.elements:
                for line in bod.nalezi:
                    if line in self.protina:
                        break
                protahni_primku(self,bod)
                self.update_protina()
                break
            pridej_bod(self,primka)

class bod:
    def __init__(self,protina:list[primka],id:str) -> None:
        self.id=id
        self.nalezi=protina
        self.spojesny_s = []
    
    def update_spojeni(self)->None:
        for bod in body:
            for primka in bod.protina:
                if primka in self.nalezi:
                    self.spojesny_s.append(bod)

    def satisfy_vertex_axiom(self):
        for bod in body:
            if bod in self.spojesny_s: continue
            


def protahni_primku(primka:primka,bod:bod)->None:
    primka.elements.append(bod)
    primka.protina.append([x for x in bod.nalezi])
    bod.nalezi.append(primka)
    bod.spojesny_s.append([x for x in primka.elements])

def pridej_primku(body:list[bod])->None:
    nprimka= primka(body)
    for bod in body:
        bod.nalezi.append(nprimka)
        nprimka.protina.append(bod.nalezi)
    primky.append(nprimka)


def pridej_bod(primka1:primka,primka2:primka)->None:
    nbod = bod([primka1,primka2],idlist[len(body)])
    primka1.elements.append(nbod)
    primka2.elements.append(nbod)
    primka1.protina.append(primka2)
    primka2.protina.append(primka1)
    body.append(nbod)


#delete later meaby useles
def disjunkt_primky(primka1:primka,primka2:primka)->bool:
    for element in primka1.elements:
        if element in primka2.elements:
            return False
    return True



