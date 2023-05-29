from kpr import idlist,body,primky,bod,primka
from kpr import pridej_bod,pridej_primku,protahni_primku,print_kprinfo

from axiom_checking import check_line_axiom,check_vertex_axiom
for it in range(4):
    body.append(bod([],idlist[it]))

pridej_primku([body[0],body[1]])
pridej_primku([body[1],body[2]])
pridej_primku([body[2],body[0]])
pridej_primku([body[3],body[0]])
pridej_primku([body[3],body[2]])

print(check_vertex_axiom(),check_line_axiom())

iterator = 0

while not check_vertex_axiom() or not check_line_axiom():
    if iterator<2:
        print_kprinfo()
    for line in primky:
        line.satisfy_line_axiom()

    if not check_line_axiom(): continue

    for vertex in body:
        vertex.satisfy_vertex_axiom()
    iterator+=1
#udělat z tohoto formátovací soubor, který bude brát .json a to konvertuje na tohle