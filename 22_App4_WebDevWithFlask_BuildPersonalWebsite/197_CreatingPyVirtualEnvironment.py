# 6'22''
# Naslov misslied-a jer zaista sukladno recenom u zadnjem videu Ard ide staviti stranicu na HirokuCloud.
# Ipak, vraca se na kreiranje VE "koji je izoliran od tvojih drugih fajlova i tvoje glavne Py-instalacije.
# Sve do sada run-ali smo Py iz glavne instalacije: to nije dobra praksa! Dobra praksa je da imas cistu instalaciju Py-a koju ces koristiti samo za svoju app i koja nece imati libraries koje ne trebas za datu app.
# Kreiranje VE sa VirtEnv Py-library: 
#? pip install virtualenv
# ne znam koliko je star video i koliko je to moderno rjesenje ali idemo naucit! Po odgovoru mog Py-a vec instalirana virtenv je kod mene 20... a kod Arda u videu 13... Znaci, video jako star!
# VE se kreira na istom levelu na kom je mapa koja drzi nas Py-fajl tj kod mene App4... Radi toga izlazim iz VSC-ea i otvaram ga ponovo unutar App4.. mape kako bi u njoj kreirao VE i nakon ulska u mapu koja sadrzi moju WebStranicu pokrecem k-du:
#? python3 -m venv virtual
#* I zaista, na levelu Demo-mape stvorila se mapa virtual!!!
# Sada moramo ponovo instalirati Flask u nasu lokalnu VE sredinu! To cinimo koristenjem pip-a iz VE dobijene mape! Sa cd idemo u tu mapu gdje lezi pip i pozivamo ga da nam instalira Flask. Dakle odradjujemo to sa sljedecom k-dom!
#? /WebsiteMySite> virtual/Scripts/pip3 install flask
# taj kod je vazio za Ardita i pip a za mene je pip3 i sve u drugoj mapi
#? /WebsiteMySite> virtual/bin/pip3 install flask 
# ni to ne radi jer Ardit ne spominje Acivate prije 
# sve skupa sumnjivo zavrsava