a = input("O‘quvchi nomini kiriting: ")

uqouvchilar = {
    "sadasd": [1, 12, 21, 12],
    "jumavoy": [131, 432, 24213],
}


if a in uqouvchilar:
    bahao = input("Bahoni kiriting: ")
    print(f"{bahao} baho qo‘shildi.")
    uqouvchilar[a] = [bahao]

elif a != uqouvchilar:
    ok = input("bunday oquvchi topilmadi oquvchi simni kirishni isasizmi: ")
    if ok == "ha":
          q = input("oquvchi ismni kiring kiritng: ")
          bk = input("bahoni kiring kiritng: ")
          print(f"{bk} baho kkiritildi")
          if  type(bk) == int:
              uqouvchilar[q] = [bk]
              print(uqouvchilar[q])
          elif type(bk) == str:
              print("iltimos faqat raqam kiritng : ")
    else:
        print("dastur tohtatiladi")
print(uqouvchilar)