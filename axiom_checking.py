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


def check_third_axiom():
    ctverice = [[a,b,c,d] for a in body for b in body for c in body for d in body]
    for C in ctverice:
        if opakuji_se_prvky(C): continue
        trojice = [[e,f,g] for e in C for f in C for g in C]

        if vsechny_trojice_na_primce(trojice):
            continue
        print(f'Čtveřice {[x.id for x in C]} má všechny trojice, které neleží na jedné přímce.')
        return True
    return False

def vsechny_trojice_na_primce(trojice:list[list[bod]])->bool:
    for T in trojice:
        if opakuji_se_prvky(T):continue
        for p in primky:
            con=False
            for bod in T:
                if bod not in p.elements:
                    con = True
                    break
            if con: continue
            return True        
    return False

def opakuji_se_prvky(ntice:list)->bool:
    for iter in range(0,len(ntice)):
        vertex = ntice[iter]
        for j in range(iter+1,len(ntice)):
            if ntice[j]== vertex:
                return True
    return False
