import cv2


def show_image_in_window():
    img = cv2.imread('rabbit.jpg')
    cv2.imshow('rabbit', img)
    cv2.waitKey(0)


def show_image_from_cam(cap):
    for i in range(30):
        cap.read()

    ret, frame = cap.read()
    cv2.imshow('', frame)

    cv2.waitKey(0)
    cap.release()


def video_recording(cap):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        out.write(frame)

        cv2.imshow('video feed', frame)

        if cv2.waitKey(0):
            break

    cap.release()
    out.release()


def recording_motions(cap):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    cap.set(3, 1280)  # установка размера окна

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)

        # перевод кадров в черно-белую градацию
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # фильтрация лишних контуров
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # метод для выделения кромки объекта белым цветом
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

        # данный метод противоположен методу erosion(),
        # т.е. эрозии объекта, и расширяет выделенную на предыдущем этапе область
        dilated = cv2.dilate(thresh, None, iterations=3)

        # нахождение массива контурных точек
        сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in сontours:
            if cv2.contourArea(contour) > 700:  # условие при котором площадь выделенного объекта меньше 700 px
                out.write(frame1)

        cv2.imshow("frame1", frame1)
        frame1 = frame2  #
        ret, frame2 = cap.read()  #

        if cv2.waitKey(40) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    # show_image_in_window()
    # show_image_from_cam(cap)
    # video_recording(cap)
    recording_motions(cap)
