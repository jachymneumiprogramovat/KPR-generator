from kpr import primky,body
from kpr import bod,primka

def check_line_axiom()->bool:
    ans = True
    #hledá jiný počet průsečíků než jedna
    for primka in primky:
        for line in primky:
            pruseciky = 0
            if primka == line:continue
            for bod in line.elements:
                if bod in primka.elements:
                    pruseciky+=1
            if pruseciky !=1:
                ans = False
                #print(f'Přímka {primka.print_elements()} má {pruseciky} průsečíků s přímkou {line.print_elements()} a to je špatně...')
    return ans

def check_vertex_axiom()->bool:
    ans = True
    for bod in body:
        for vertex in body:
            if bod==vertex:continue
            usecky=[]
            for primka in primky:
                if bod in primka.elements and vertex in primka.elements:
                    usecky.append(primka)
            if len(usecky)!=1:
                ans = False
                #print(f'Body {bod.id} a {vertex.id} se protínají na {len(usecky)} přímkách')
    return ans

#zkontrolovat třetí axiom