# 5'04''
# Znaci konfigurirati path-ove za novi app unutar /mysite/urls.py fjla i njegove varijable-liste "urlpatterns" unutar koje vec imamo 2 patha ('admin/' i 'blog.url')
# dodajemo: path('translate', include('translator.urls')) gdje je urls fajl unutar mape translator koji ne postoji i kojeg kreiramo odmah iza ovog kao urls.py u koji stavljamo ostale url-ove kojima je root dio .../translate/...
# za pocetak ardi samo kopira urlove iz blog/urls.py-a i brise slug-path koji nije dio transappa a potom i path-about i ostaje samo sa "path('', views.PostList.as_view(), name='home')" kojeg mjenja u ""