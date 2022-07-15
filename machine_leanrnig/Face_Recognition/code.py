import cv2


## Function for locating a face in an image
def face_rec(img_dir):
    # Reading the image
    img = cv2.imread(img_dir)

    # converting the image to gray color
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # getting the holiday from machine model
    FaceRecog = cv2.CascadeClassifier('face_recog_data.xml')

    # Getting the coordinates
    cor = FaceRecog.detectMultiScale(gimg, 1.3, 5)

    try:
        if cor.all():
            for (x, y, w, h) in cor:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

            return img
    except AttributeError:
        return None

cv2.imshow('Face',face_rec('peoples.jpg'))
cv2.waitKey()

## working in jupyter