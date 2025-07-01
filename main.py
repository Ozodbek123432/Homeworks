a = input("oquvhi nomi kriting: ")

uqouvchilar = {
    "sadasd": [1, 12, 21, 12],
    "jumavoy": [131, 432, 24213],
}

if a in uqouvchilar:
    bahao = input("baxni krting: ")
    try:
        bahao = int(bahao)
        if 0 <= bahao <= 5:
            uqouvchilar[a].append(bahao)
            print(f"{bahao} bax qoshlidi.")
        else:
            print("0...5 orasid bah kriting")
    except:
        print("raqam yozsan kn")

elif a != uqouvchilar:
    ok = input("bu oquvhchi yoq, qoshsinmi? ha/yoq: ")
    if ok == "ha":
        q = input("oquvchini ismini bering: ")
        bk = input("baxni yoz: ")
        try:
            bk = int(bk)
            if 0 <= bk <= 5:
                uqouvchilar[q] = [bk]
                print(uqouvchilar[q])
            else:
                print("bah 0 bilan 5 orasda bolsinda")
        except:
            print("raqam yoz, boshqa narsa emas")
    else:
        print("dastr tuktatild")
