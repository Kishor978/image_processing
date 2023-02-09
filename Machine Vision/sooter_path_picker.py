import cv2
import numpy as np
import pickle

polygons = []  # for all polygon and their points
path = []

img = cv2.imread("E:\image processing\Machine Vision\imgBoard.png")

# function to get the location of mouse clicks


def mousePoints(event, x, y, flags, parms):
    if event == cv2.EVENT_LBUTTONDOWN:
        path.append([x, y])


while True:
    print(path)
    for point in path:
        cv2.circle(img, point, 7, (0, 0, 255), cv2.FILLED)

    pts = np.array(path, np.int32).reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    key = cv2.waitKey(0)

    # press w for entering the score and press enter for further polygons
    if key == ord('w'):
        score = int(input("Enter score: "))
        polygons.append([path, score])
        print("total polygon:", len(polygons))
        path = []

        # press on the top of window
        #  press p for seving the file and closing the window
    if key == ord("p"):
        with open('E:\image processing\Machine Vision\polygons', "wb")as f:
            # print(polygons)
            pickle.dump(polygons, f)
        break
