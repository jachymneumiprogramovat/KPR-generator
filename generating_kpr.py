from axiom_checking import check_line_axiom,check_vertex_axiom,check_third_axiom,check_fourth_axiom
from kpr import primky, body



def built_kpr():
    while not check_vertex_axiom() or not check_line_axiom():
        for line in primky:
            line.satisfy_line_axiom()

        if not check_line_axiom(): continue

        for vertex in body:
            vertex.satisfy_vertex_axiom()