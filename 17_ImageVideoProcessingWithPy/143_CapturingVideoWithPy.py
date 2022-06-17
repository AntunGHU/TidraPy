# 19'45''
# kako bi prikazivali video a ne samo 1. frame koristimo while-loop u koji cemo uvuci sve od L:check do L:cv2.wait

import cv2, time

video = cv2.VideoCapture(0)       # 0-builtin camera, 1,2,..-neke druge kamere,  "movie.mp4"-ako vec imamo video
a=0
while True:                       # da bi relanu promjenu vidjeli umjesto 0 stavljamo 2000 (2s) u L:cv2.waitKey. Smanjujem i slee na 1 sek, i za sada sve prekidam silom ^C. sto nije radilo pa sam morao citav term u smece cime se kamera ugasila!! Komamo L:time i uvodimo kondicional  sa novouvedenom varijablom key=cv2.waitKey(2000)
    a+=1
    check, frame = video.read()

    print(check)                       # True
    print(frame)                        # Matrica

    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY) # konverzija u sive nijanse i ponovo isprobavanje - sve radi!!
    time.sleep(1)
    cv2.imshow("Capturing",gray)   # kreiranje objekta koji ce video pokazati

    key=cv2.waitKey(1)                  # definiranje zatvaranja videa (isto kao i kod slike); # vidim da nisam promjenio 0 na 2000, mozda je to razlog zasto nisam uspio zaustaviti term
    
    if key==ord('q'):                   # dakle zatvaranje samo sa q-tipkom: probao sa play i sve radilo!!! Bravo Ardi! Dodaje poslije svega varijablu a za brojanje fremova!
        break

print(a)                    # i dok kod njega broj framevoa 51 kod mene samo 9, zasto?
video.release()                 # nakon snimanja otpust kameri
cv2.destroyAllWindows()           # brisanje RAM-a (kao i kod slika)
# Play i Ardi kaze da je na svojoj vidio paljenje svjetla ali da poneko ponekad zbog brzine to ne uspjeva vidjeti! Zato "time"
# Probavam i ja i zaista sve radi!
# pri kraju isprobava sa pokrivanjem kamere i pokazuje kako se brojevi matrice pretvaraju u nulu, kod mene opet bas i ne!
# dakle, imam problem s brzinom snimanja kamere! Mozda driveru lx-u!