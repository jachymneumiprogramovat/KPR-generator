from kpr import idlist,body,primky,bod,primka
from kpr import pridej_bod,pridej_primku,protahni_primku,print_kprinfo

for it in range(4):
    body.append(bod([],idlist[it]))

pridej_primku([body[0],body[1]])
pridej_primku([body[0],body[2]])
pridej_primku([body[2],body[3]])

pridej_bod(primky[0],primky[2])


print_kprinfo()

