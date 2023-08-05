import cv2

frame0 = cv2.VideoCapture(0)
frame1 = cv2.VideoCapture(2)

state = False

while 1:
    # teknik switch camera
    # kamera tidak literally berjalan bersamaan, tapi bergantian, ini ditujukan untuk menurunkan CPU usage

    if state:
        ret0, img0 = frame0.read()
        img1 = cv2.resize(img0,(360,240))
        if (frame0):
            cv2.imshow('img1',img1)
    else:
        ret1, img00 = frame1.read()
        img2 = cv2.resize(img00,(360,240))
        if (frame1):
            cv2.imshow('img2',img2)
    state = ~state # state = bukan state

    

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

frame0.release()
frame1.release()
cv2.destroyAllWindows()




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
