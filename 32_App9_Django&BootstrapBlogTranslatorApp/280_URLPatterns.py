# 15'16''
# unatoc sumni koju naslov izaziva, ipak ce unositi dummy datas u db-table! koristenjem db browsera radi testiranja (inace ce se unositi kroz admin-interface)
# Nakon unesenog jednog reda idemo povezati nas red sa views.py. Za to cemo koristiti fajl /blog/urls.py
# Nakon svih edita i save-nja geska: "AttributeError: type object 'BlogView' has no attribute 'as_view'"
# ide i importe django.generic i prekidamo scriptu i ponovo startamo i sad greske vise nema!!!
# poslije probava vidjeti dogs zapis na mysites na localhost ali greska (koja je drugacija od potrage za necim sto uopce ne postoji kao npr cats).
# nakon kontrole imena nalazi problem u settings.py i variabli dir koja je prazna a trebala bi imati unos TEMPLATES_DIR kojeg mene u DIR ali i citavu L-definciju premjesta iznad TEMPLATES {_DIR:} kako bi isti bio definiran prije upotrebe - kod py-a se ide po redu!!
# i sada osvjezavam dogs-stranicu i pojavljuje se moj dummy-zapis iz db-a!!!