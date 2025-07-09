def s(son):
    son = int(input("son kriting"))
    almal = input("almal kritng")
    son1 = int(input("2 son kriting"))
    if almal == "+":
        return son + son1
    elif almal == "-":
        return son - son1
    elif almal == "*":
        return son * son1
    elif almal == "/":
        return son / son1
print(s("qimat"))