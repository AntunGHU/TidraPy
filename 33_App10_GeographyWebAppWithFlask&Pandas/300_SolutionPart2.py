# 16'21''
# 16'21
# Objasnjenje pocinje slikom mapa i fajlova projekta i izjavom da prilozena mapa jest finalna verzija tog programa. No postoje razlike onog sto vidim na slici videa i onog sto mapa /298 app10-geocoder donosi.
# mapa donosi 3 podmape i 1 app.py fajl dok video pocinje sa 4 app1,2,3,4.py fajla i 4 mape(static, templates, uploads i virtual) Ard ce to objasniti i pokazati i kod svakog razvojnog fajl tako da pravim razvojnu verziju "App10_eval"
# prva stvar koju je napravio je stvaranje static-folder structure (4 nazvane mape od kojih su static i templates standardi za Flask appse)
# uploads mapa je za usere za download
# mapa virtual je dir virtualnog env kako se onda radilo sa kdom:
#? python -m virtualenv virtual
# i mapa virtal imala je fresh copy of python, pip itd. Za naglasiti je da je u finalnoj verziji vise nema!!!
# potom je instalirao flask i pandas i geopy u virtual mapu virtenva
# potom se stvaraju interfacei kroz fajlove index.html i download.html. Prvo obicni html bez {} tagova! Vidi u gotovu verziju! Takodjer na pocetku nije imao <div> tag sa {}. 
# Potom je isao u static i kreirao main.css te oblikovao tagove templates-fajlova! Nije se zelio baviti objasnjavanjem css fajla jer je selfexplanatory
# zatim se vraca u index.html i referencira u head-tagu na /static/main.css
# malo disgresije: neki developeri startaju sa FE a neki s BE kraja
# nakon napravljenog interfejsa kreira 1.2.3.4. verziju app-fajla - i ja napravio! Na zalost, svaka ima u sebi gresaka tako da sam ih morao komati!
# slusajuci arda ipak shavcam da to ne ide! pocetnici moraju ici prema kompleksnosti polagano. neide drugacije!!!
#! NASTAVAK s videom part2
# objasnjava 3. verziju koja je bez greske!!!