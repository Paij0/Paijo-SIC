import cv2
import threading

def capture_camera(camera_id):
    camera = cv2.VideoCapture(camera_id)

    while True:
        ret, frame = camera.read()

        if not ret:
            print(f"Failed to grab frame from camera {camera_id}")
            break

        cv2.imshow(f'Camera {camera_id}', frame)

        # Stop capturing when pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Start capturing from camera 0 (outdoor camera)
    thread_outdoor = threading.Thread(target=capture_camera, args=(0,))
    thread_outdoor.start()

    # Start capturing from camera 2 (indoor camera)
    thread_indoor = threading.Thread(target=capture_camera, args=(2,))
    thread_indoor.start()

    # Wait for the threads to finish
    thread_outdoor.join()
    thread_indoor.join()
