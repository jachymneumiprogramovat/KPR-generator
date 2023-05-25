idlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]

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
        if primka not in self.protina:
            self.protina.append(primka)
    
    def satisfy_line_axiom(self)->bool:
        """Danou přímku propojí se všemi se kterými zatím není propojená. Defaultně protahuje, když není možnost tak přidá nový bod."""
        #Problém s tím, že to kontroluje jen orientovanou dvojici přímek
        #a předtím než to zkusí druhou orientaci to vynese rozsudek
        #proto musí nejdřívě zkusit najít na "cag" volný bod pro "ef" to když nevyjde
        #tak zkusit najít volný bod na "ef" pro "cag"
        #proto to asi budu muset přepsat na nějakou obecnou funkci, která dostane dvojici
        #a zkusí to pro obě permutace. Pak by to mělo být chill
        for primka in primky:
            if primka in self.protina: continue
            for bod in primka.elements:
                if self.print_elements()==['c', 'a', 'g']:
                    self.print_primkainfo()
                    bod.print_bodinfo()
                con =False
                for line in bod.nalezi:
                    if line in self.protina:
                        con = True
                        break
                if con: continue
                protahni_primku(self,bod)
                break
            pridej_bod(self,primka)

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
        """Pocitá s tím, že line axiom je splněný. Daný bod spojí se všemi body se kterými není spojený."""
        volne_body=[self]
        for bod in body:
            if bod in self.spojeny_s: continue
            volne_body.append(bod)
        if len(volne_body)==1: return
        pridej_primku(volne_body)

def protahni_primku(primka:primka,bod:bod)->None:
    """Přidá do přímky bod a zároveň updatuje všechny seznami"""
    print(f'Protahuji přímku {primka.print_elements} o bod {bod.id}')
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
    print(f'Přidávám novou přímku {nprimka.print_elements()}')
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
    print(f'Nový bod {nbod.id} je průsečíkem {primka1.print_elements()} a {primka2.print_elements()}')

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