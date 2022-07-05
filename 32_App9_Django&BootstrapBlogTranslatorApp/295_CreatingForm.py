# 5'29''
# kreiramo editiranjem fajla /translator/views.py
# editamo: def translator_view(request):
#               return render(request, 'translator.html')
# rerun server i nema nisata na http://127.0.0.1:8000/translate
# popravljam u urlovima trnslate u translate/ i pojavljuje se stranica ali sa oznakom greske u translator.html i naglasava da translator_get je problem. Mjenjam to u translate_view takoda bude u skladu sa onim u urls.py i to dovodi do pojave polja za unos i prijevod kao i gumba "Submit". Medjutim, gumb ne radi
# popravak gumba opet u translator.html tako damdodamo red izmedju Form i div tagova: {% csrf_token %}
# to polupopravlja gumb jer umjesto greske klik na njega dovodi do nestnka unesenog teksta za prijevod!
