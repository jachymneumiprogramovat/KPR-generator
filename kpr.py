class primka:
    def __init__(self,elements:list[int]) -> None:
        self.elements=elements
        pass
    def sort(self,bod)->None:
        if self not in protina[bod]:
            protina[bod].append(self)

body=[1,2,3,4]
protina={}
for bod in body:
    protina[bod]=[]

primky=[
    primka([1,3]),
    primka([3,2]),
    primka([1])
]


def protni():
    for bod in protni:
        for cara in primky:
            cara.sort(bod)

protni()
print(protina)

def disjunkt(list1,list2):
    """Vrací true jen když dva listy nemají žádný stejný prvek"""
    for node in list1:
        if node in list2:
            return False
    return True,node



for line in primky:
    for cara in primky:
        if disjunkt(line.elements,cara.elements):
            for node in line.elements:
                for bod in cara.elements:
                    if disjunkt(protina[bod], protina[node]):
                        print(protina[bod],protina[node])
                        line.elements.append(bod)
                        cara.elements.append(node)
                        
print("debug")
for cara in primky:
    print(cara.elements)

print(protina)
                    
                          










