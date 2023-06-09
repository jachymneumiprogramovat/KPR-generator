from kpr import primky,body
from kpr import bod,primka

def check_line_axiom()->bool:
    #print("checking lina axiom",len(body))
    """Kontroluje jestli každá přímka se protiná s každou druhou právě jednou"""
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
    #print("checking veretx axiom",len(body))
    """Kontroluje jestli každými dvěma body prochází právě jedna přímka"""
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


def check_third_axiom()->bool:
    #print("checking third axiom")
    """Kontroluje jestli existuje čtveřice bodů taková že žádná její podmnožina velikosti tři neleží na jedné přímce"""
    ctverice = [[a,b,c,d] for a in body for b in body for c in body for d in body]
    for C in ctverice:
        if opakuji_se_prvky(C): continue
        trojice = [[e,f,g] for e in C for f in C for g in C]

        if vsechny_trojice_bodu_na_primce(trojice):
            continue
        print(f'Čtveřice {[x.id for x in C]} má všechny trojice, které neleží na jedné přímce.')
        return True
    return False


def check_fourth_axiom():
    """Kontroluje jestli existuje čtveřice přímek taková že žádná její podmnožina velikosti tři se neprotíná v jednom bodě"""
    ctverice = [[a,b,c,d] for a in primky for b in primky for c in primky for d in primky]
    for C in ctverice:
        if opakuji_se_prvky(C):continue
        trojice = [[e,f,g] for e in C for f in C for g in C]
        if vsechny_trojice_primek_v_bodu(trojice):
            continue
        return True
    return False 

def vsechny_trojice_primek_v_bodu(trojice:list[list[primka]])->bool:
    """Pro všechny trojice přímek kontroluje jestli existuje bod ve kterém se všechny protínají """
    for T in trojice:
        if opakuji_se_prvky(T):continue
        for b in body:
            con = False
            for p in T:
                if b not in p.elements:
                    con = True
                    break
                if con:continue
                return True
    return False

def vsechny_trojice_bodu_na_primce(trojice:list[list[bod]])->bool:
    """Pro všechny trojice bodů kontroluje jestli existuje primka na ktere lezi"""
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
    """Kontroluje jestli se v ntici neopakuji prvky"""
    for iter in range(0,len(ntice)):
        vertex = ntice[iter]
        for j in range(iter+1,len(ntice)):
            if ntice[j]== vertex:
                return True
    return False