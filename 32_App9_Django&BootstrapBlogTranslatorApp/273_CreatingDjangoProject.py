# 11'12''
# pocinje sa komandom "django-admin startproject mysite ." gdje tocka znaci da ce se projekt formirati i korespondni fajlovi postaviti u dir "." tj u tekuci dir
# kao rezultat stvaraju se mapa "mysite" (level a9env-a) i fajl manage.py
# unutar mape mysite: __init__.py (prazan za pocetak a kasnije mozemo staviti stvari koje zelimo pokretati kad app starta)
# mysite/asgi.py: konfig fajl kojeg mozda budemo poslije mjenjali pri deployanju app-a na asgi-server
# mysite/wsgi.py: konfig fajl kojeg mozda budemo poslije mjenjali pri deployanju app-a na wsgi-server
# mysite/settings.py: sve postavke ala time_zone, language, itd
# mysite/url.py: postavke url-ova
# manage.py: obicno ga ne mjenjamo i koristan je dok gradimo projekt za pokretanje ala:
#? python manage.py runserver   # Starting development server at http://127.0.0.1:8000/
# sto nam daje otprilike isto kao i kad smo pokretali flask. ^Klik i otvara
#? python manage.py migrate     # izvrsava quaeries i kreira db.sqlite3 (po defu koristi sqlite3 ali na serveru se lako upari sa postgresql)
# admin se dobija sa http://127.0.0.1:8000/admin ali prvo moramo formirati admin usera!