while True:
    # Ask the user if they want to start the test
    c = input("Testni boshlashni xohlaysizmi ha/yoq? ").lower()
    b1 = 0
    if c == "ha":
        print("Test boshlandi!")

        # --------------------------------------------------------------------------------------------------------------------

        print("Savol: A javob togri ?")
        print("A) Bu javobni toping")
        print("B) Bu javobni toping")
        print("C) Bu javobni toping")
        print("D) Bu javobni toping")
        d = input("Javobingizni kiriting (A, B, C, D): ").upper()
        if d == "A":
            print("To'g'ri javob!")
            b1 += 10
        else:
            print("Noto'g'ri javob.")
        print("2:keyingi savol")

        # --------------------------------------------------------------------------------------------------------------------

        print("Savol: B javob togri?")
        print("A) Bu javobni toping")
        print("B) Bu javobni toping")
        print("C) Bu javobni toping")
        print("D) Bu javobni toping")
        d = input("Javobingizni kiriting (A, B, C, D): ").upper()
        if d == "B":
            print("To'g'ri javob!")
            b1 += 10
        else:
            print("Noto'g'ri javob.")
        print("3:keyingi savol")

        # --------------------------------------------------------------------------------------------------------------------

        print("Savol: C javob togri ?")
        print("A) Bu javobni toping")
        print("B) Bu javobni toping")
        print("C) Bu javobni toping")
        print("D) Bu javobni toping")
        # Get the user's answer
        d = input("Javobingizni kiriting (A, B, C, D): ").upper()
        if d == "C":
            print("To'g'ri javob!")
            b1 += 10
        else:
            print("Noto'g'ri javob.")
        print("4:keyingi savol")
        # --------------------------------------------------------------------------------------------------------------------

        print("Savol: D javob togri ?")
        print("A) javobni toping")
        print("B) javobni toping")
        print("C) javobni toping")
        print("D) javobni toping")
        d = input("Javobingizni kiriting (A, B, C, D): ")
        if d == "D":
            print("To'g'ri javob!")
            b1 += 10
        else:
            print("Noto'g'ri javob.")
    # --------------------------------------------------------------------------------------------------------------------

    elif c == "yoq":
        print("Test tugatildi.")
    else:
        print("Noto'g'ri kiritish. Iltimos, 'ha' yoki 'yoq' deb kiriting.")
    print(f"test tugadi  yigilgan bal 40/{b1}%")