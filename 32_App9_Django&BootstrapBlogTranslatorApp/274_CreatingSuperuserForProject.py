# 4'00''
# pocinje s ponavljanjem sta smo uradili do sad i napominje da k-da "python manage.py runserver " ponekad vrati gresku "The port is already in use" sto je znak da django proj vec run-a na nekom terminalu! Pogasimo pa restart
# da bi kreirali usera zaustavljamo dj-pr sa ^+C pa kdu:
#? python manage.py createsuperuser
# Kreira se sa unosom imena usera (ostavio prazno pa je "antun"), email:"antun.jerkovic@gmail.com", pass:xxxxxxDJ # Superuser created successfully.
# pokrecemo dj-pr ponovo i u admin: i prijavljujem se kao superuser - uspjevam!!!