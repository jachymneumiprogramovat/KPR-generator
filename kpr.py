body = []#seznam vsech bodu
primky=[]#seznam vsech primek

class primka:
    """Trida pro primky"""
    def __init__(self,elements:list[object]) -> None:
        self.elements=elements
        self.protina = [self]
        self.id = "".join([x.id for x in self.elements])
    
    def updateid(self)->None:
        """Aktualizuje self.id z self.elements"""
        self.id = "".join([x.id for x in self.elements])
    
    def get_primkainfo(self)->dict:
        """Vrati vsechny informace o primce"""
        return {
            "jsem primka:":self.id,
            "protinam":[x.id for x in self.protina]
        }

    def update_protina(self,primka)->None:
        """Prida do self.protina jen kdyz tam ta primka uz neni"""
        if primka not in self.protina:
            self.protina.append(primka)
    
    def satisfy_line_axiom(self)->bool:
        """Danou přímku propojí se všemi se kterými zatím není propojená. Defaultně protahuje, když není možnost tak přidá nový bod."""
        
        for primka in primky:
            if primka in self.protina: continue
            if spoj_primky(self,primka):
                protahni_primku(spoj_primky(self,primka)[0],spoj_primky(self,primka)[1])
            else:
                pridej_bod(self,primka)

class bod:
    """Trida pro vsechny body"""
    def __init__(self,nalezi:list[primka],id:str) -> None:
        self.id=id
        self.nalezi=nalezi
        self.spojeny_s = [self]
    
    def get_bodinfo(self)->dict:
        """Vrati vsechny informace o bodu"""
        return {
            "jsem bod":self.id,
            "spolecny bod primek":[primka.id for primka in self.nalezi],
            "spojeny s":[x.id for x in self.spojeny_s]
        }
    
    def update_spojeni(self,spojenci:list[object])->None:
        """Prida bod do self.spojeny_s jen kdyz tam uz neni"""
        for bod in spojenci:
            if bod not in self.spojeny_s:
                self.spojeny_s.append(bod)

    def satisfy_vertex_axiom(self):
        """Pocitá s tím, že line axiom je splněný. Daný bod spojí se všemi body se kterými není spojený."""

        volne_body=[self]
        for bod in body:
            if bod in self.spojeny_s: continue
            volne_body.append(bod)
        if len(volne_body)==1: return
        pridej_primku(volne_body)


def spoj_primky(primka1:primka,primka2:primka)->tuple[primka,bod]:
    """Když existujou vrací bod a přímku takovou aby se přímka dala prodloužit o bod"""

    for bod in primka1.elements:
        con =False
        for line in bod.nalezi:
            if line in primka2.protina:
                con=True
                break
        if con: continue
        return [primka2,bod]
    
    for vertex in primka2.elements:
        cont = False
        for lin in vertex.nalezi:
            if lin in primka1.protina:
                cont = True
                break
        if cont: continue
        return [primka1,vertex]
    return False
        
def protahni_primku(primka:primka,bod:bod)->None:
    """Přidá do přímky bod a zároveň updatuje všechny seznami"""

    print(f'Protahuji přímku {primka.id} o bod {bod.id}')
    primka.elements.append(bod)
    primka.updateid()
    bod.nalezi.append(primka)

    for x in bod.nalezi:
        primka.update_protina(x)
        x.update_protina(primka)
    for x in primka.elements:
        bod.update_spojeni([x])
        x.update_spojeni([bod])
    

def pridej_primku(body:list[bod])->None:
    """Vytvoří novou přímku z bodů. Zjistí s jakými všemi přímkami se protíná"""

    nprimka= primka(body)
    print(f'Přidávám novou přímku {nprimka.id}')
    for bod in body:
        bod.update_spojeni(body)
        for x in bod.nalezi:
            nprimka.update_protina(x)
            x.update_protina(nprimka)
        bod.nalezi.append(nprimka)
    primky.append(nprimka)

def pridej_bod(primka1:primka,primka2:primka)->None:
    """Vytovří nový bod jako průnik dvou přímek ty upraví jako, že se protínají."""

    from inout import idlist
    nbod = bod([primka1,primka2],idlist[len(body)])
    print(f'Nový bod {nbod.id} je průsečíkem {primka1.id} a {primka2.id}')

    primka1.elements.append(nbod)
    primka2.elements.append(nbod)
    primka1.updateid()
    primka2.updateid()
    primka1.protina.append(primka2)
    primka2.protina.append(primka1)
    #změnit pořadí když to bude nutné kvůli rychlosti
    for vertex in primka1.elements:
        vertex.update_spojeni([nbod])
    for vertex in primka2.elements:
        vertex.update_spojeni([nbod])

    body.append(nbod)
    nbod.update_spojeni(primka1.elements)
    nbod.update_spojeni(primka2.elements)