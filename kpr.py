idlist = ["a","b","c","d","e","f","g","h","i","j","k"]

body = []
primky=[]

class primka:
    def __init__(self,elements:list[object]) -> None:
        self.elements=elements
        self.protina = [self]
    
    def print_elements(self)->list:
        return ([x.id for x in self.elements])
    
    def print_primkainfo(self)->None:
        print("jsem přímka:",self.print_elements())
        print([x.print_elements() for x in self.protina])

    def update_protina(self,primka)->None:
        print(primka not in self.protina,primka.print_elements())
        if primka not in self.protina:
            self.protina.append(primka)
    
    def satisfy_line_axiom(self)->bool:
        """Vraci true, když line axiom platí pro danou přímku."""
        satisfies = True
        for primka in primky:
            if primka in self.protina: continue
            for bod in primka.elements:
                for line in bod.nalezi:
                    if line in self.protina:
                        break
                protahni_primku(self,bod)
                satisfies = False
                break
            pridej_bod(self,primka)
            satisfies=False
        return satisfies

class bod:
    def __init__(self,nalezi:list[primka],id:str) -> None:
        self.id=id
        self.nalezi=nalezi
        self.spojeny_s = [self]
    
    def print_bodinfo(self):
        print(self.id)
        print([primka.print_elements() for primka in self.nalezi])
        print([x.id for x in self.spojeny_s])
    
    def update_spojeni(self,spojenci:list[object])->None:
        for bod in spojenci:
            if bod not in self.spojeny_s:
                self.spojeny_s.append(bod)

    def satisfy_vertex_axiom(self):
        """Pocitá s tím, že line axiom je splněný. Vraci true, když je vertex axiom splěný pro daný bod."""
        for bod in body:
            if bod in self.spojeny_s: continue
            pridej_primku(self,bod)

def protahni_primku(primka:primka,bod:bod)->None:
    """Přidá do přímky bod a zároveň updatuje všechny seznami"""
    primka.elements.append(bod)
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
    for bod in body:
        bod.update_spojeni(body)
        for x in bod.nalezi:
            nprimka.update_protina(x)
            x.update_protina(nprimka)
        bod.nalezi.append(nprimka)
    primky.append(nprimka)

def pridej_bod(primka1:primka,primka2:primka)->None:
    """Vytovří nový bod jako průnik dvou přímek ty upraví jako, že se protínají."""
    nbod = bod([primka1,primka2],idlist[len(body)])

    primka1.elements.append(nbod)
    primka2.elements.append(nbod)
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

def print_kprinfo():
    print("Nejdříve body:")
    for vertex in body:
        vertex.print_bodinfo()
    print("Teď přímky:")
    for line in primky:
        line.print_primkainfo()