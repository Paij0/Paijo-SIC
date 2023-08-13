# import cv2
# import time

# timer_cam0 = time.time()
# timer_cam2 = time.time()


# frame0 = cv2.VideoCapture(0)
# frame1 = cv2.VideoCapture(2)

# state = False

# while 1:
#     # teknik switch camera
#     # kamera tidak literally berjalan bersamaan, tapi bergantian, ini ditujukan untuk menurunkan CPU usage
#     if state:
        
#         try:
#             ret0, img0 = frame0.read()
#             img1 = cv2.resize(img0,(360,240))
#             if (frame0):
#                 cv2.imshow('img1',img1)
#         except:
#             print(f"delta lost cam0: {time.time() - timer_cam0} s")
#             timer_cam0 = time.time()
#     else:
        
#         try:
#             ret1, img00 = frame1.read()
#             img2 = cv2.resize(img00,(360,240))
#             if (frame1):
#                 cv2.imshow('img2',img2)
#         except:
#             print(f"delta lost cam2: {time.time() - timer_cam2} s")
#             timer_cam2 = time.time()
    

#     state = ~state # state = bukan state

#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
    

# frame0.release()
# frame1.release()
# cv2.destroyAllWindows()




# # import cv2

# # frame0 = cv2.VideoCapture(0)
# # frame1 = cv2.VideoCapture(2)

# # state = False

# # while True:
# #     # Teknik switch camera
# #     # Kamera tidak secara fisik berjalan bersamaan, tapi bergantian, ini ditujukan untuk menurunkan CPU usage
# #     state = not state  # state = bukan state (membalik nilai state)

# #     if state:
# #         ret0, img0 = frame0.read()
# #         if ret0:
# #             cv2.imshow('Camera 1', img0)
# #     else:
# #         ret1, img1 = frame1.read()
# #         if ret1:
# #             cv2.imshow('Camera 2', img1)

# #     k = cv2.waitKey(30) & 0xFF
# #     if k == 27:  # Tekan 'Esc' untuk keluar
# #         break

# # frame0.release()
# # frame1.release()
# # cv2.destroyAllWindows()




# import cv2

# frame0 = cv2.VideoCapture(0)
# frame1 = cv2.VideoCapture(2)

# state = False

# while True:
#     state = not state

#     if state:
#         ret0, img0 = frame0.read()
#         if ret0:
#             cv2.imshow('Camera 1', img0)
#         else:
#             print("Failed to read from Camera 1")
#     else:
#         ret1, img1 = frame1.read()
#         if ret1:
#             cv2.imshow('Camera 2', img1)
#         else:
#             print("Failed to read from Camera 2")

#     k = cv2.waitKey(30) & 0xFF
#     if k == 27:
#         break

# frame0.release()
# frame1.release()
# cv2.destroyAllWindows()


# import cv2
# import time

# frame0 = cv2.VideoCapture(0)
# frame1 = cv2.VideoCapture(2)

# state = False

# while True:
#     # teknik switch camera
#     # kamera tidak secara harfiah berjalan bersamaan, tapi bergantian, ini ditujukan untuk menurunkan CPU usage

#     if state:
#         ret0, img0 = frame0.read()
#         if ret0:
#             img1 = cv2.resize(img0, (360, 240))
#             cv2.imshow('img1', img1)
#     else:
#         ret1, img00 = frame1.read()
#         if ret1:
#             img2 = cv2.resize(img00, (360, 240))
#             cv2.imshow('img2', img2)

#     state = not state  # state = bukan state

#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break

# frame0.release()
# frame1.release()
# cv2.destroyAllWindows()



import cv2
import time

# Inisialisasi kamera
frame0 = cv2.VideoCapture(0)
frame1 = cv2.VideoCapture(2)

# Setel resolusi rendah
frame_width = 360
frame_height = 240
frame0.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
frame0.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
frame1.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
frame1.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# Inisialisasi timer
timer_cam0 = time.time()
timer_cam2 = time.time()

state = False

while True:
    if state:
        ret0, img0 = frame0.read()
        if ret0:
            cv2.imshow('Camera 0', img0)
        else:
            print(f"Delta lost cam0: {time.time() - timer_cam0} s")
            timer_cam0 = time.time()
    else:
        ret1, img1 = frame1.read()
        if ret1:
            cv2.imshow('Camera 1', img1)
        else:
            print(f"Delta lost cam2: {time.time() - timer_cam2} s")
            timer_cam2 = time.time()

    state = not state

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Tutup kamera dan jendela
frame0.release()
frame1.release()
cv2.destroyAllWindows()
