# 21'55''
# Prvi video sa VSC!!!
# Kreiram poseban fajl "main.py" cije ime unaprijed ide prema pravilima koja cemo poslije morati postivati!
# takodjer se kreira fajl "design.kv"
# takodjer u 3 odjeljak vsc-ea stavlja sliku dizajna buduce aplikacije - i ja je napravio sa printscreen
# 2 nacina kreiranja mob-appa sa py i kivy library: 1. napisati sve u py - logiku, grafsucelje itd - sto nije dobra praksa, 2. pravljenje grafinterfacea in kivy in kivy language koji je vrlo jednostavan i kog mozemo nauciti u 1 danu!
# radit cemo na ovaj drugi nacin!!
# pocinjemo sa potrebnom logikom u main-py
# kako nebi upisivao u path digi naziv mojih mapa premjestam design.kv u root mapu projekta "Tidra" a isto cinim i sa main.py. Treba na kraju da ih izjednacim sa onima u mapi App6
# Tjekom rada na kv-fajlu instaliram kivy extension
# >>> dir(App) je jos jednom ukucano u py-shelu da bi dobio sve built-in metode klase App!!!
# nakon "if __name..." pokrecem main i dobivamo okvir ali ne kakav smo ocekivali iako u terminalu nema gresaka! U takvim slucajevima treba gledati kod u kv fajlu. Dodaje cols:1 u glavni GridLayout (iako je rekao da ne treba) pa ponovo provjerava i vec bolje!
# Dodaje cols:1 i sljedecem Layout-u i sad je dosta bolje!
# Na kraju summary: zahvaljujuci kv fajlu nemoramo u py importati npr GridLayout ili Buttonse - to on cini za nas!
# Malo o hijerarhiji unutar  kivi: najvisi je App(MainApp), potom ide ScreenManager koji je reprezentan sa RootWidget, a onda dodje Screen koji se reprezenta sa LoginScreen-om
# Svu navedenu hijerarhiju dokazuje izmjenjenim kodom kv-fajla kojim je dokazuje, jer se nista ne mjenja!