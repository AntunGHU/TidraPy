# 5'00''
# library koja to rjesava je pyinstaller
# instalacija sa komandom
#? pip3 install pyinstaller
# nakon toga je teribly easy to make py-executable script!!
# izvrsavamop k-du 
#? pyinstaller CodingFrontendInterface.py 
# tj u fokusu je glavna py-scripta koja importa onu drugu i basu!
# ako se k-da ostavi takvom, pyinstaller ce kreirati executable za os u kom je zajedno sa jos nekim fajlovima koji olaksavaju pregled i detekciju greski itd, ali ako zaista hocemo samo jedan fajl onda dodajemo parametar --onefile. Takodjer je uobicajeno dodati i parametar --windowed kako se nebi otvarao komandline. Dakle
#? pyinstaller --onefile --windowed CodingFrontendInterface.py
# k-da se izvrsava u terminalu
# Kao rezultat u svakom os-u stvaraju se 2 mape: build i dist. Unutar build mape imamo niz fajlova specificiranih za os a u dist samo jedan izvrsni fajl!! U LX-u se rakodjer pokrece kao i u Win-u sa run! Pokretanjem, odmah se executable-fajlu u mapi dist pridruzuje database books.db