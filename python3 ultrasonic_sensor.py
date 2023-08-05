import RPi.GPIO as GPIO
import time

# Atur pin sesuai dengan mode BCM
GPIO.setmode(GPIO.BCM)

# Tentukan pin Trig dan Echo
TRIG_PIN = 21
ECHO_PIN = 20

# Atur pin sebagai output dan input
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def distance_measurement():
    # Nyalakan sinyal ultrasonik selama 10 mikrodetik
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Catat waktu saat sinyal ultrasonik dikirimkan
    start_time = time.time()

    # Inisialisasi variabel untuk waktu pantulan gelombang ultrasonik
    pulse_start = 0
    pulse_end = 0

    # Catat waktu saat pulsa pertama kali diterima
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Catat waktu saat pulsa terakhir diterima
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Hitung selisih waktu pantulan untuk mendapatkan durasi
    pulse_duration = pulse_end - pulse_start

    # Hitung jarak berdasarkan kecepatan suara (dalam sentimeter)
    # Kecepatan suara umumnya sekitar 34300 cm/detik pada suhu kamar
    # Jarak = (kecepatan suara * waktu) / 2 (karena bolak-balik)
    distance = (34300 * pulse_duration) / 2

    return distance

try:
    while True:
        distance = distance_measurement()
        print(f"Jarak: {distance:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    # Jika program berhenti, atur pin GPIO ke mode default
    GPIO.cleanup()
