def a():
    ism = input("iismni kirintg:")
    yosh = int(input("yoshi kirintg:"))

    if 5 <= yosh and 60 >= yosh:
        return f"Siz {ism} chipta narhi 30$"
    elif yosh < 5 and yosh > 60:
        return "chipta narhi150$"
    else:
        return "chipta tekin"

print(a())
