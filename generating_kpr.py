from axiom_checking import check_line_axiom,check_vertex_axiom,check_third_axiom,check_fourth_axiom
from kpr import primky, body



def built_kpr():
    """Dokud nejsou splněné axiomi 1. a 2. tak se opakuje funcke tříd bod,primka aby je splnina"""
    while not check_vertex_axiom() or not check_line_axiom():
        for line in primky:
            line.satisfy_line_axiom()

        if not check_line_axiom(): continue

        for vertex in body:
            vertex.satisfy_vertex_axiom()
    if not check_third_axiom():
        print("Vygeneroval jsi takový trochu zkriplený případ KPR. Nesplňuje 3. axiom")