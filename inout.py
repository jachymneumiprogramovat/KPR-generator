from kpr import body,primky,bod
from kpr import pridej_primku

import json


def load_starting_position():
    data = json.load(open("starting.json"))
    global idlist
    idlist = data["idlist"]

    for _ in range(data["#bodu"]):
        body.append(bod([],idlist[len(body)]))

    for ntice in data["primky"]:
        pridej_primku([body[i] for i in ntice])


def output_kprinfo():
    bodyinfo = [bod.get_bodinfo() for bod in body]
    primkainfo = [primka.get_primkainfo() for primka in primky]
    with open("kpr.json","w") as outputfile:
        outputfile.write("Nejdrive body:")
        outputfile.write(json.dumps(bodyinfo,indent=2))
        outputfile.write("Ted primky:")
        outputfile.write(json.dumps(primkainfo,indent=2))