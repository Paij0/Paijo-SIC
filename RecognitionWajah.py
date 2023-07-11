import cv2
import joblib
import face_recognition

# Path untuk model yang dilatih
MODEL_PATH = 'latihfile.pkl'

# Load model yang dilatih
model = joblib.load(MODEL_PATH)

# Load cascade classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fungsi untuk ekstraksi vektor encoding wajah menggunakan library face_recognition
def extract_face_encoding(image):
    # Menggunakan face_recognition library untuk ekstraksi vektor encoding
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_image)

    if len(face_encodings) > 0:
        return face_encodings[0]

    return None

# Dictionary untuk memetakan label ke nama
label_to_name = {
    0: "dhifa",
    1: "Paijo",
    2: "kazi",
    # Tambahkan entri lain sesuai dengan jumlah kelas yang ada
}

# Mulai pengenalan wajah menggunakan webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        face_encoding = extract_face_encoding(roi_gray)

        if face_encoding is not None:
            # Memprediksi label wajah menggunakan model yang dilatih
            label = model.predict([face_encoding])[0]

            # Mengubah label menjadi nama menggunakan dictionary
            name = label_to_name.get(label, "Unknown")

            # Menandai wajah dengan kotak dan label
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    # Menghentikan pengenalan wajah dengan menekan tombol 'q' atau 'esc'
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:  # 'q' atau 'esc'
        break

camera.release()
cv2.destroyAllWindows()
