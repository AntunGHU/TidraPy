# 2'39''
# mala prakticna tipa: nemoram gasiti terminal radi aktiviranja virtenva, dovoljno je klik na plus za novi terminal koji ce se otvoriti sa aktiviranim virtenvom!!!
# TranslatorApp (TA) ce biti novi item na nasoj homepage. Da bi ga dodali prvo zaustavljamo sa ^+C server
# pisemo kdu u termu:
#? python manage.py startapp translator
# pojavljuje se novokreirana mapa "translator"
# sada zelimo registrirati buducu aplikaciju u /mysite/settings.py i to u varijablu INSTALLED_APPS i to ispod unosa kojeg smo napravili za prvu app "blog".
# Time smo kreirali praznu DjangoAplikaciju