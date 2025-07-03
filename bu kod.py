# verrsya 2  git add  .
l = {
    "sas": 27421347,
}
while True:
     s = input("malumoot qidirish")
     if s not in l:
         b = input("maluumot topilmadi isim kiring")
         a = input("raqam kiring  ")
         l [b] = a
     for x, v in l.items():
         if x == s:
             print(v)
