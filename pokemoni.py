#dva typy ludi:  jedno/dvojzlozkovy
#budu v skupinách rozlozený
#ako 1z utočí na 1z
#ako 1z utoči na 2z
#ako 2z utoči na 1z
import json
attackfield = {}
subor = json.load(open("effectiveness.json", "r"))
helper = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}
#for key in helper.keys():
#    print(key)


#for key,value in helper.items():
#    print(key,value)
for strengt in subor:
    for attacker in subor[strengt]:
        if attacker not in attackfield.keys():
            attackfield[attacker] = {}
        for defender in subor[strengt][attacker]:
            attackfield[attacker][defender] = helper[strengt]


def attack(p1: int, p2: int, army: str) -> tuple:
    temp = army.split(",")
    army1 = temp[:p1]
    army2 = temp[p1:p1 + p2]
    f1 = 0
    f2 = 0
    for pokemon1 in army1:
        for pokemon2 in army2:
            najlepsi = 0
            for typ1 in pokemon1.strip().split():
                sila = 1
                for typ2 in pokemon2.strip().split():
                    sila = sila * attackfield[typ1][typ2]
                if sila > najlepsi:
                    najlepsi = sila
            f1 = f1 + najlepsi
    for pokemon1 in army2:
        for pokemon2 in army1:
            najlepsi = 0
            for typ1 in pokemon1.strip().split():
                sila = 1
                for typ2 in pokemon2.strip().split():
                    sila = sila * attackfield[typ1][typ2]
                if sila > najlepsi:
                    najlepsi = sila
            f2 = f2 + najlepsi
    f1 = round(f1, 1)
    f2 = round(f2, 1)
    if f1 > f2:
        vitaz = "ME"
    elif f2 > f1:
        vitaz = "FOE"
    else:
        vitaz = "EQUAL"
    return (f1, f2, vitaz)
print(attack(2, 6, "Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))
