while True:
      a = input("soz kiriting: ")
      soz  = []

      if a == a[::-1]:
          soz.append(a)
          print(soz)
      else:
          print(f"{a} bu soz tneg emas")