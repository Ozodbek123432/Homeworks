def text_to_binary(text):
    binary = ""
    for char in text:
        ascii_value = ord(char)  # Harfni raqamga
        binary_char = bin(ascii_value)[2:]  # Raqamni 2-likka
        binary_char = binary_char.zfill(8)  # 8 bit qilib to‘ldirish
        binary += binary_char + " "
    return binary.strip()


def binary_to_text(binary_input):
    letters = binary_input.split()
    text = ""
    for binary_char in letters:
        ascii_value = int(binary_char, 2)  # 2-likdan 10-likka
        harf = chr(ascii_value)  # Raqamdan harfga
        text += harf
    return text


# === Cheksiz menyu ===
while True:
    print("\n🧠 2-lik Konvertor")
    print("1. Matnni 2-likga o‘tkazish")
    print("2. 2-likni matnga o‘tkazish")
    print("3. Chiqish")

    tanlov = input("Tanlang (1, 2 yoki 3): ")

    if tanlov == "1":
        soz = input("So‘z kiriting: ")
        natija = text_to_binary(soz)
        print("Ikkilik (2-lik):", natija)

    elif tanlov == "2":
        binary = input("0 va 1’lardan iborat kod kiriting (har harf orasida bo‘sh joy):\n")
        natija = binary_to_text(binary)
        print("Matn:", natija)

    elif tanlov == "3":
        print("Dastur yakunlandi. 👋")
        break

    else:
        print("❌ Noto‘g‘ri tanlov! Faqat 1, 2 yoki 3 ni kiriting.")
