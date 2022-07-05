# 10'09''
# postoje 2 http-requesta: 1.) od strane usera za ipadresom npr: "example.com/translate/" ili "127.0.0.1:8000/translate/" i koji je get-request i koji se obradjuje sa path-om iz /translator/urls.py/urlpatterns/path "path('', views.translator_view, name='translator_view')" i s njimpovezanim fajlom /mysite/urls.py/urlpatterns/path "path('translate/', include('translator.urls'))" koji zajedno formiraju jedinstven url kao u npr /example... i
# 2.) kad user pritisne Submit button koji je POST-request i koji pristupa url-u preko linije "<form action="{% url 'translator_view' %}" method="post">" iz translator.html koji dalje ide prema translator_view-u inutar fajla /translator/urls.py  i linije "path('', views.translator_view, name='translator_view')" dakle istom pathu kao i get-reguest.
# to moramo promjeniti u ovom videu, tj odvojiti ova dva zahtjeva i izvoditi različite akcije s njima. Za sada zelimo da kad user unosi tekst kojeg zeli prevesti i pritisne "Submit", da se unutar drugog box-a, gdje ce se kasnije pojaviti prijevod, pojavljuje verzija s velikim slovima
# prvo moramo uvesti razliku izmedju requestsova unutar fajla /translator/views.py sto cinimo sa "if..." itd i uspjeeli!! No, ostao je problem u nestajanju orginalonog teksta sto treba rjesiti
# problem se moze razumjeti iz "if..." unutar fajla /translator/views.py jer se iz njega vidi da on u konacnici renderira samo jedan box. Problem se rijesava ako u render-output liniju "return render(request, 'translator.html', {'output_text':output})" dodamo i original text kad ona postaje "return render(request, 'translator.html', {'output_text':output, 'original_text':original_text})". Da bi to radilo opet moramo kao i sa output_text-om, i sa original_text-om u translator.html i liniju "<textarea class="form-control" rows="3" name="my_textarea"></textarea>" koja posataje "<textarea class="form-control" rows="3" name="my_textarea">{{original_text}}</textarea>." I sad orginalni ostaje a izlazni s velikim slovima se pojavljuje!!!
# I sa ovime je dovrsen Django dio: imamo funkcionalnu web-app, i sad sve sto jos ostaje je da umjesto izlaza koji je trenutno Kapitalizirani ulaz (vidi /translator/views.py liniju "output = original_text.upper()") dobijemo prevedeni i vraceni ulaz sa nekim drugim paketom!!! (googletranlator-paket spominjan na pocetku)