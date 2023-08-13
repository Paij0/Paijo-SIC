import cv2
import threading

def read_camera(camera_index, output):
    camera = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = camera.read()
        if ret:
            frame_resized = cv2.resize(frame, (360, 240))
            output[camera_index] = frame_resized
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()

if __name__ == "__main__":
    frame0, frame1 = [None]*2
    thread0 = threading.Thread(target=read_camera, args=(0, frame0))
    thread1 = threading.Thread(target=read_camera, args=(2, frame1))

    thread0.start()
    thread1.start()

    state = False

    while True:
        if state:
            if frame0 is not None:
                cv2.imshow('Camera 0', frame0)
        else:
            if frame1 is not None:
                cv2.imshow('Camera 2', frame1)
        state = not state

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    thread0.join()
    thread1.join()
    cv2.destroyAllWindows()
