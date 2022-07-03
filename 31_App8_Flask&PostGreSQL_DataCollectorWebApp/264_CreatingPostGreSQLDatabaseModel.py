# 18'17''
# Video kreiranja base s PGS. Zabiljeske koje cemo poslije takodjer prebaciti u root Tidra projkta
# Pri pokretanju pgAdmin4 dobio poruku da imam verziju 6.10 a aktualna je 6.11 sto me nagnalo da malo pogledam mogucnosti upgradea sto me dovelo do scripti za instal apt - verije
# #
# Setup the repository
#

# Install the public key for the repository (if not done previously):
#?sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

# Create the repository configuration file:
#?sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

#
# Install pgAdmin
#

# Install for both desktop and web modes:
#?sudo apt install pgadmin4

# Install for desktop mode only:
#?sudo apt install pgadmin4-desktop

# Install for web mode only: 
#?sudo apt install pgadmin4-web 

# Configure the webserver, if you installed pgadmin4-web:
#?sudo /usr/pgadmin4/bin/setup-web.sh


# Nisam zelio gubiti vrijeme i nastavljam sa ovom verzijom. Oba se spajamo sa PGS Serverima, moj je AntunPGS! Klikom na Databases dobijamo trenutne base: kod mene samo "postgres" db. Kreiramo preko pgAdmin4 novu db za ovu aplikaciju: visina_mail_collector, ovnera ostavljam postgres.
# Kreirali smo db ali nemamo tablicu a nju cemo kreirati koristeci py!
# Kad smo kreirali db u Bookstore App-u koristili smo library psycopg2 koji bi mogli i ovdje ali puno koristeniji library za kom sa db unutar Flask aplikacija je "SQLAlchemy" koji je more high level od psycopg2 i nemoramo praciti conn ili closati kao u psycopg2. Ali posto je nastao na osnovu psycopg2 moramo instalati oba u nas virtenv:
#? pip3 install psycopg2 
# Nije islo kao nisam imao potrebne preduvjete u source. Predlozio mi instal pip3 install psycopg2-binary sto sam prihvatio i uspjesno odradio iako ne znam jel to to. I Ardit ima problema koje pokusava rjesiti sa pip-upgrade ali nije to rjesilo pa je otisao prcompile psycopg2 cjelo vrijeme naglasavajuci da vjerovatno nemam tih problema ako sam na Mac or Linux
# Nakon sto je rjesio svoje probleme ide i instalira SQLAlchemy i ja snjim Uspjesno sa k-dom
#? pip3 install Flask-SQLAlchemy
# potom idemo u app.py i nastavljamo prvo sa importanjem SQLAlchemy itd
# Na zalost, import SQLAlchemy ne radi i prinudjen sam prekinuti!! Ok, bar neke stvari oko virtualenv-a smo u ovoj APP naucili!
# u konacnici importam citav flask sto bi mozda islo ali sam izgubio volju da ovo pratim dalje, mozda se vratim. ali ne, ni to ne radi!!!