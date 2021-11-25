import cv2

red_min = [0, 69, 100]
red_max = [0, 100, 69]

green_min = [120]

blue_min = [240]

def color_of_central_pixel():
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()

    while cap.isOpened():
        ret, frame = cap.read()
        hcv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        height, width = hcv_img.shape[:2]
        color = hcv_img[int(height / 2), int(width / 2)]
        # if color[0] < 60:
        #     print("Красный")
        # elif color[0] < 120:
        #     print("Зеленый")
        # else:
        #     print("Синий")
        #
        print(color)

        cv2.line(hcv_img, (int(width / 2), 0), (int(width / 2), height), (int(color[0]), int(color[1]), int(color[2])))
        cv2.line(hcv_img, (0, int(height/2)), (width, int(height/2)), (int(color[0]), int(color[1]), int(color[2])))

        cv2.imshow("frame1", hcv_img)

        if cv2.waitKey(40) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


color_of_central_pixel()
