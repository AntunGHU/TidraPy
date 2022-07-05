# 6'12''
# Na pocetku Ard objasnjava da postoji minor problem sa paketom "googletrans" ali koji se moze izbjeci instalacijom author verzije paketa "googletrans==4.0.0-rc1". On je instalao tu verziju a ja cu probati prvu s k-dom 
#? pip install googletrans
# ako ne bude radilo onda cu kao i Ard instalati njegovu sa k-dom
#? pip install googletrans==4.0.0-rc1
# nakon instalacije isprobava prvo ulaskom u python sa
#? python
# a potom isprobava tako sto prvo sa kdom:
#? >>> from googletrans import Translator
# a potom s k-dom 
#? >>> translation = Translator()
# kreira translacijsku instancu od importane Translator klase te sa 
#? >>> translation.translate(text="How did you learn Python?", dest='de').text
# provjerava rad paketa, kod njega dobro kod mene ne pa ideminstalati isto sto i on i sad radi i kod mene!!!
# vrlo brzo sam probavanjem nasao da je za hrvatski 'hr', ruski 'ru', engleski 'en' nakon sto sam ukucao hrvatski tekst (kojeg je automatski prepoznao - fantastikus!)
# Za kraj uvoda i komandnog djela translatora i primjeri koje sam mu dao za prevod na en:
#* >>> translation.translate(text="Danas konačno završavam rad na Django poglavlju!", dest='en').text # 'Today I finally finish working on Chapter Django!'
# i za ruski
#* >>> translation.translate(text="Danas konačno završavam rad na Django poglavlju!", dest='en').text # 'Сегодня я наконец -то заканчиваю работать над главой Django!'
#! A sad dalje sa videom !!
# posto sam se preko terma uvjerio da Translator paket radi taj term-kod treba napisati negdje unutar django-appa
# radimo to prvo kreirajuci poseban fajl translate.py unutar mape adekvatne app tj u /translator/translate.py mapi u ovom slucaju i u njega upisujem kde terma. Ipak Ard tu ne ide kao u termu nego koristi funcion!!! Ta funkcija ce u nasem fajlu /translator/views.py (
    #! kojem prvo na pocetak dodajemo "from . import translate" a koje mene nagoni na misao da bez mape a9env u kojoj se nalaze moje instalirane stvari i py zapravo nema sanse da ista radi, tj nemogu je izbjeci pa je rjesenje imati u svakom projektu env mape ali ih iskljuciti iz git-a sa gitignore)    
# zamjeniti L "output = original_text.upper()" koji postaje "output = translate.translate(original_text)"
# potom ard dovrsava funkciju unutar /translator/translate.py tako da ona izgleda
#? def translate(text):
#?     translation = Translator()
#?     translation= translator.translate(text=text, dest='de')
#?     return translation.text
# iako bih ja radije da mogu ici sa 
#? def translate(text, dest):
#?     translation = Translator()
#?     translation= translator.translate(text=text, dest=dest)
#?     return translation.text
# tako da mogu mjenjati destinacijski jezik, ali ne znam kako bih to prosljedio u graf sucelje p zato ostavljam ardovu verziju za sada
# Snimamo, isprobavamo i radi hrvatski na njem, ru, en naravno uz moje intervencije u kod sa 'de', 'ru', 'en'
# Jos nam za kraj ostaje dodavanje Meni-itema "Translator" na home-pageu!
# prvo idemo u "base.html", kopirano jedan li-tag i pastamo ispod te ga prilagodjavamo tako da naziv postane "Translator" a u django tag stavljamo 'translator_view' kojeg za sigurnost ocitavamo-copyamo iz /translator/urls.py
# F5 i Gumb "Trnslator" se pojavio!
#todo Ovdje Ard zavrsava sa App9 projektom sa rjecima da vjeruje da bi ovo trebalo biti dosta da startamo sa Djangom. Pokrili smo par vaznih funkcionalnosti Django-a: rukovanje s db-iima, dobavljanje i procesuiranje userova inputa i vracanje outputa useru!!
