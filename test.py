def shifrlash(matn, siljish=3):
    natija = ""
    for harf in matn:
        if harf.isalpha():
            kod = ord(harf) + siljish
            if harf.islower():
                if kod > ord('z'):
                    kod -= 26
                natija += chr(kod)
            elif harf.isupper():
                if kod > ord('Z'):
                    kod -= 26
                natija += chr(kod)
        else:
            natija += harf
    return natija

matn = input("Yashirin xabar yoz: ")
sirli = shifrlash(matn)
print("🔐 Shifrlangan:", sirli)
