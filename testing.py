from kpr import idlist,body,primky,bod,primka
from kpr import pridej_bod,pridej_primku,protahni_primku,print_kprinfo

for it in range(5):
    body.append(bod([],idlist[it]))

pridej_primku([body[0],body[1],body[2]])
pridej_primku([body[1],body[4]])

protahni_primku(primky[1],body[3])


print_kprinfo()

