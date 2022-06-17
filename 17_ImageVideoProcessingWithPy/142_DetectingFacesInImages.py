# 19'39''
# enter poslije , zareza, Py tretira kao nastavak linije koda
# ; unutar linije i py tretira kao drugu liniju koda
# nakon sto sve dobro radi do 19'35'', predlaze isto nalazenje lica sa slike news.jpg. Ja SaveAs - vidi 142a

import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")     # bez dodatnih parametara, read as it is
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # konvertiranje BRG u GRAY

faces=face_cascade.detectMultiScale(gray_img,
     scaleFactor=1.05,  # piramida kao objasnjenje
     minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

print(type(faces))      # <class 'numpy.ndarray'>
print(faces)            # [[157  84 379 379]]   # kordinate lica

resized=cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))  # [1]-sirina?, [0]-visina

# cv2.imshow("Gray",gray_img) # komano nakon ulaska for-a kako bi vidjeli img
cv2.imshow("Gray",resized) 
cv2.waitKey(0)
cv2.destroyAllWindows()