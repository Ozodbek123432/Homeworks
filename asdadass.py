import json
import time
import random
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from googlesearch import search

class Utils:
    @staticmethod
    def clean_text(text):
        return text.strip().lower()

    @staticmethod
    def get_random_response(arr):
        return random.choice(arr)

    @staticmethod
    def format_time():
        try:
            return datetime.now().strftime("%H:%M:%S")
        except:
            return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def limit_messages(msgs, limit=100):
        return msgs[-limit:]

    @staticmethod
    def is_valid_input(text):
        return 0 < len(text) <= 500

    @staticmethod
    def save_messages(msgs, filename="chat_messages.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(msgs, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Xabarlar saqlashda xato: {e}")

    @staticmethod
    def load_messages(filename="chat_messages.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Xabarlar yuklashda xato: {e}")
            return []

    @staticmethod
    def save_memory(text, filename="memories.json"):
        try:
            memories = Utils.load_memories(filename)
            memories.append({"text": text, "timestamp": Utils.format_time()})
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(memories, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Eslatma saqlashda xato: {e}")

    @staticmethod
    def load_memories(filename="memories.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Eslatmalar yuklashda xato: {e}")
            return []

    @staticmethod
    def check_for_spam(text):
        return len(text) > 1000 or "http" in text or "www" in text

    @staticmethod
    def add_random_emoji(text):
        emojis = ['😊', '🚀', '🌟', '😄', '🎉', '🇺🇿', '🥘', '🎶', '❤️', '✨']
        return text + " " + Utils.get_random_response(emojis)

    @staticmethod
    def get_random_joke():
        jokes = [
            "Nega kompyuter o‘zbekcha gapirdi? Chunki u o‘zbekona AI edi! 😄",
            "Palov nima deydi? 'Meni yeb ko‘r, men mazaliman!' 🥘",
            "Nega non o‘zbekona? Chunki u tandirdan chiqadi! 😊"
        ]
        return Utils.get_random_response(jokes)

    @staticmethod
    def get_random_proverb():
        proverbs = [
            "Sabrning oxiri – omonlik!",
            "Mehnatning mevasi shirin bo‘ladi!",
            "Yaxshi so‘z – yurakka davo!"
        ]
        return Utils.get_random_response(proverbs)

    @staticmethod
    def get_random_poem():
        poems = [
            "O‘zbek yuragi – muhabbat bog‘i,\nSevgi bilan to‘lgan har bir yo‘li.",
            "Samarqand ko‘kda porlaydi yulduz,\nO‘zbekona ruhda sevgi – cheksiz!"
        ]
        return Utils.get_random_response(poems)

    @staticmethod
    def google_search(query, num_results=3):
        try:
            results = []
            for url in search(query, num_results=num_results, lang="uz"):
                response = requests.get(url, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()[:200]
                results.append({"url": url, "text": text})
            return results
        except Exception as e:
            print(f"Google qidiruvda xato: {e}")
            return []

    @staticmethod
    def save_search_results(query, results, filename="search_knowledge.json"):
        try:
            knowledge = Utils.load_search_results(filename)
            knowledge.append({"query": query, "results": results, "timestamp": Utils.format_time()})
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(knowledge, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Qidiruv natijalarini saqlashda xato: {e}")

    @staticmethod
    def load_search_results(filename="search_knowledge.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Qidiruv natijalarini yuklashda xato: {e}")
            return []

def generate_ai_response(input_text):
    clean_input = Utils.clean_text(input_text)
    response = "Uzr, bu savolga javobim yo‘q, lekin boshqa savol so‘rasang, yordam beraman, jonim! 😊 “Hazil”, “maqol” yoki “she’r” so‘ra!"

    responses = {
        'salom': 'Assalomu alaykum, azizim! 😊 Kayfiyating yaxshimi? Yordam kerakmi? 💖',
        'qalaysan': 'Zo‘rman, rahmat! Sen-chi, qanday yuribsan? 😇💬',
        'vaqt': f"Hozir soat {Utils.format_time()}. Suhbatlashamizmi? ⏰",
        'isming': 'Men O‘zbekona AI – sening do‘sting! 🥰 Sen kimsan? 🤗',
        'hazil': Utils.get_random_joke(),
        'maqol': Utils.get_random_proverb(),
        'she’r': Utils.get_random_poem(),
        'o‘zbekiston': 'O‘zbekiston – qalbimning go‘zalligi! 🇺🇿 Qaysi viloyatdan? 🗺️',
        'eslab qol': 'Xop, bu xabarni eslab qoldim, jonim! 😍 “Eslat” deb yoz! 💾',
    }

    if "eslab qol" in clean_input:
        Utils.save_memory(input_text)
        response = "Xop, eslab qoldim, azizim! 😍 “Eslat” deb yozsang, ko‘rsataman! 💾"
    elif "eslat" in clean_input:
        memories = Utils.load_memories()
        response = "Mana eslatmalarim, jonim! 😊\n" + "\n".join([m["text"] + " (" + m["timestamp"] + ")" for m in memories]) if memories else "Hozircha eslatma yo‘q, azizim! 😔"
    elif "o‘rgan" in clean_input or "qidir" in clean_input:
        query = input_text.replace("o‘rgan", "").replace("qidir", "").strip()
        if query:
            response = f"{query} haqida qidiryapman, jonim! 😎"
            search_results = Utils.google_search(query)
            if search_results:
                Utils.save_search_results(query, search_results)
                response += "\nTopdim:\n" + "\n".join([f"{r['url']}: {r['text'][:50]}..." for r in search_results])
            else:
                response += "\nAfsus, hech narsa topolmadim! 😔 Boshqa savol so‘ra!"
        else:
            response = "Nima qidiray, azizim? 😄 Aniqlik kirit! 💖"

    for key in responses:
        if key in clean_input:
            response = responses[key] if isinstance(responses[key], str) else responses[key]()
            break

    knowledge = Utils.load_search_results()
    for item in knowledge:
        if item["query"] in clean_input:
            response += f"\nAvval {item['query']} haqida shuni bilardim: {item['results'][0]['text'][:50]}... 😊"

    if random.random() > 0.6:
        facts = ["O‘zbekistonda 12 ta viloyat bor!", "Palov – UNESCO ro‘yxatida!"]
        response += " Aytgancha, " + Utils.get_random_response(facts)
    return Utils.add_random_emoji(response)

def add_message(text, sender):
    try:
        timestamp = Utils.format_time()
        print(f"{sender}: {text} ({timestamp})")
        return {"text": text, "sender": sender, "timestamp": timestamp}
    except Exception as e:
        print(f"Xabar qo‘shishda xato: {e}")
        return None

def main():
    global messages
    print("Assalomu alaykum! Men O‘zbekona AI, suhbatga tayyorman! 😄 “Hazil”, “maqol”, “she’r” yoki “o‘rgan nima gap” deb so‘ra, jonim! 💖")
    messages = Utils.load_messages()
    for msg in messages:
        print(f"{msg['sender']}: {msg['text']} ({msg['timestamp']})")

    while True:
        try:
            user_input = input("Siz: ")
            if user_input.lower() in ["chiqish", "exit", "stop"]:
                print("Xayr, azizim! 😊 Yana ko‘rishamiz! 💖")
                break

            if not Utils.is_valid_input(user_input):
                print("Xabar yoz, yoki qisqa tut, jonim! 😔")
                continue

            if Utils.check_for_spam(user_input):
                print("Spamga o‘xshaydi! Oddiy savol so‘r, azizim! 😊")
                continue

            msg = add_message(user_input, "Siz")
            if msg:
                messages = Utils.limit_messages(messages + [msg])
                Utils.save_messages(messages)

            print("AI javob yozmoqda...")
            time.sleep(1.2)
            ai_response = generate_ai_response(user_input)
            msg = add_message(ai_response, "AI")
            if msg:
                messages = Utils.limit_messages(messages + [msg])
                Utils.save_messages(messages)

        except KeyboardInterrupt:
            print("\nXayr, azizim! 😊 Yana ko‘rishamiz! 💖")
            break
        except Exception as e:
            print(f"Xato: {e}. Yana urinib ko‘r, jonim! 😊")

if __name__ == "__main__":
    main()