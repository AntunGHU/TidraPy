# 8'15''
#? python manage.py startapp imeappa # "blog"
# formira se u root-u dj-pr mapa istog imena kao i imeappa, u nasem slucaju "blog"
# unutar blog-mape: mapa "migrations" i nekoliko py-fajlova: __init__, admin, apps, models, tests, views
# migrations mi ne modificiramo i sadrzi sve db-migracije tj promjene (specificno unutar /blog/migrations/__init__ fajla)
# blog/__init__.py:takodjer obicno necemo modificirati osim ako zelimo nesto da se izvodi pri startu blog-app-a
# blog/admin.py: kod vezan za administrativne funkcije
# blog/apps: config za app koji takodjer ne mjenjamo
# blog/models: jedna od tri glavne komponente web-seit-a koja sadrzi db-polja wb.seita; npr ime, autor, sadrzaj itd
# blog/views: druga od tri glavne komponente web-seit-a koja sadrzi ili py-funcs ili py-classe koji su midleman izmedju nasih definiranih polja u models i html-koda tj templatesa kao 3. komponente!!
# blog/tests.py: za pisanje testova za testiranje app-a kad je ready
# na kraju pravi promjene u fajlu /mysite/settings.py. Idemo do odjeljka "INSTALED_APPS" i listi koja sadzi defaultne iteme-appse dodati nasu 'blog', !! bitno uociti da odstupa od standardnog zapisa liste imajuci zarez iza zadnjeg iteme prije zagrade!!!
# sad smo spremni dodavati sadrzaj u blog-app