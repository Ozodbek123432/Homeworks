# from glati import *
# print(a(12,21))

def s(card):
    a= (card[::-4])
    b = "*" * (len(card) - 4)
    return b + a



print(s("1234152273981112"))
print(s("1234152273981143"))
print(s("1234432432424222"))
