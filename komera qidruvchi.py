import cv2
from datetime import datetime
# Yuzni aniqlash uchun klassifikator yuklash
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamera ishga tushirish
cap = cv2.VideoCapture(0)
 
while True:
    # Kadrni o'qish
    ret, frame = cap.read()
    if not ret:
        break

    # Rasmni kulrang rangga aylantirish
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) > 0:
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f"Yuz aniqlandi: {current_time}")

    # Aniqlangan yuzlarni belgilash
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Natijani ko'rsatish
    cv2.imshow('Yuz Aniqlash', frame)

    # 'q' tugmasini bosish orqali chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Resurslarni ozod qilish
cap.release()
cv2.destroyAllWindows()