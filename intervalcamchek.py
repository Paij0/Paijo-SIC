import cv2

def check_available_cameras():
    num_cameras = 10  # Cek hingga indeks kamera 9

    for i in range(num_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera {i} is available")
            cap.release()
        else:
            print(f"Camera {i} is not available")

if __name__ == "__main__":
    check_available_cameras()
