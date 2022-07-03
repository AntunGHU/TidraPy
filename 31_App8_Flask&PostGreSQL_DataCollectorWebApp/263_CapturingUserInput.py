# 17'31''
# video u kom ce se pisati py-dio. Pocinje sa kreiranjem virtual environmenta sto znaci lokalno instaliranje i mnogo fajlova. Kako to sve nebi utjecalo na moj git odlucujem nastaviti ovaj App8 u posebnoj mapi u koju cu kopirati dosad napravljeno i reopen u vsc. Kasnije cu sve vratiti na orginalnu lokaciju ali bez git-nepotrenbosti
# pravim virtenv sa kdom koja je mozda stara sto ce biti interesantno provjeriti na App sa PostgreSQL
#? pip3 install virtualenv
# poruka da je vec instaliran modul virtenv ali da bi mozda trebao upgredati pip. posto meni stalno javlja oko verzije pip-a odlucujem probati k-du sa arditovog screena ako ce ici
#? python3 -m pip install --upgrade pip
# i isla je i nadogradila pip - nadam se da mi vise nece slati poruke
# nakon sto smo se uvjerili da py ima u sebi virtenv modul, koristimo ga za instal virtenv-a za ovaj projek s komandom "python -m venv virtual" za Winse a sa "python -m virtualenv virtual" za Lin i Mac gdje je kod svih virtual ime mape virtual koja ce se formirati u sklopu projekta. Morao dodati 3 u kdu
#? python3 -m virtualenv virtual
# i zaista! kreirala se mapa virtual!!!
# pregledavamo mapu i sadrzaj i utvrdjujem da je moja mapa sasvim drugacijeg sadrzaja od ardove- rezultat promjena od prvog nastanka ardovog videa
# sljedece ide instalacija Flaska koristenjem pip-a iz mape /virtual/Script/pip kod Arda "App8/virtual/Script...." ali ja nemam mapu Script pa cu koristiti pip iz mape /bin dakle:
#? /virtual/bin/pip3 install flask
# ali!!! u nastavku Ardit kaze da je to samo jedan nacin ali da ce on sada koristiti drugi i to je /virtual/Script/activate sto je za mene 
#? source ~/Documents/aCod/App8/virtual/bin/activate
# i dobio sam (virtual) ispred prompt-grupe!!! znak da sam u venv-u!!!
# kao i Ardit pokazao sam si da se sad sve odnosi na virtenv. npr which python dalo mi je python iz enva
# potom smo instalirali flask u env sa
#? pip3 install flask
# i provjerio flask sa "which flask" i dobio "home/antun/Documents/aCod/App8/virtual/bin/flask"
# kreiramo app.py u App8 mapi i prelzimo tamo
# nakon ispisanog koda provjeravamo rad aktivirajuci app.py pomocu python-a iz virtenv-a koji mora biti aktiviran u konzoli kako bi se virtpy koristio
# Ardit dobija nakon pokretanja app.py-a sa komandom "python app.py" odgovor da app radi na http://127.0.0.1:5000 <Press ^+c za izac>, Restarting with start, Debugger is active, Debugger pin code.... Potom pokrece Browser i ide na local host:5000 i pojavljuje se nasa index stranica
# ja to idem probati prvo sa gumbom start i aktiviranim virtual u terminalu i... !!!! Dobio sve kao i Ard
# probavamo submit-ati i ne javlja nam se ni success stranica jer je nismo map-ali u app.py-u pa to idemo dodati dodavanjem jos jednog reda @app.route("/success")
# Medjutim!!!, taj dodani red nam omogucava da vidimo stranicu success kao /success ali se jos nije linkala sa nasim submit-butonom!! Da bi to radilo oznaku success-stranice u nasem index.html-fajlu prilagodjavamo sa "form action="success.html"" na oblik za flask tj form action="{{url_for('success')}}". Nakon te izmjene pokusaj submit-anja daje sad drugaciju gresku "Method not allowed" zato sto je u index-u odredjen POST metod a u app.py je get metod default. Ako hocemo POST moramo to promjeniti
# To mjenjamo dodavanjem eksplicite oznake "method=['POST']" u @app.route...
# Nakon sto smo uspjesno poslali podatke trebamo ih capturati i Promjene u app koje ce to omogućiti: te promjene radimo u sklopu definicije "def success"