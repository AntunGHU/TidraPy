# py-fajl i image u istom dir-u pa ne moramo path sa slikom
# 0-za black-white-one bat; 1 za citanje slike kakva je tj rgb-3 bat; -1 za mogucnost transpoza i sa alfa-kanalom

import cv2
from cv2 import resize
img=cv2.imread("galaxy.jpg",0)
print(img)  
#[[14 18 14 ... 20 15 16]
#[12 16 12 ... 20 15 17]
#[12 13 16 ... 14 24 21]
#...
#[ 0  0  0 ...  5  8 14]
#[ 0  0  0 ...  2  3  9]
#[ 1  1  1 ...  1  1  3]]
print(type(img))    # <class 'numpy.ndarray'>
print(img.shape)    # (1485, 990)
print(img.ndim)    # 2

# resiziranje slike kako bi stala na ekran
# resized_image=cv2.resize(img,(1000,500)) # py ce interpolirati piksele na zeljene vrijednosti
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) # py ce piksele prepoloviti, int mora biti!

# za pokaz resizane slike, zatvaranje uz odgodu navodjenjem milisekundi
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
# cv2.waitKey(2000) # gasi se nakon 2 sek
cv2.waitKey(0) # ne gasi se do pritiska na bilo koju tipku
cv2.destroyAllWindows()

#! Kao i kroz App1, i ovdje je kod mene lokacija py-fajla drugacija od lokacije projekta i terma pa se lokacija slike kad se cita i pise poklapa sa lokacijom prompta tj u root-u projekta!!!