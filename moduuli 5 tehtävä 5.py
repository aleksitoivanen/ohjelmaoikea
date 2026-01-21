yritykset = 0
while yritykset < 5:
    acco = input("Syötä käyttäjätunnus: ")
    pasw = input("Syötä salasana: ")
    if acco == "python" and pasw == "rules":
        print("Tervetuloa")
        break
    else :
        print("pääsy evätty")
        yritykset += 1

if yritykset == 5:
    print("olet yrittänyt liian monta kertaa")


