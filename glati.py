from numpy.ma.core import append


def s(a,b):
    while True:
        a = int(input("son kritng"))
        b = []
        b.append(a)
        r = int(input("kvadratga oshrish uchun son kriting"))
        c = a ** r
        return c
print(s("qimat","2qimanrt"))