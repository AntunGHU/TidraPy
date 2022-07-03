# 12'42''
# VE je samo kopija nase Py-instalacije
# Posebno dobro za WebDev jer omogucava WebServeru da ima spisak potrebnih librarija
# Sada se pravi drugacije, sa venv builtin library! Takodjer cemo raditi sa py 3.10
#? python3.9 -m venv env
# nakon toga klik na verziju Py-a i izbor PyInterpretera koji uz sebe nosi ('env':venv) a u termu ispred prompt grupe je ('env')
# kod mene nema env!?!? tj nije aktiviran! Ipak!!! Potrazio i nasao odgovore!!!
#! When I try to create venv it throws this error:
# Error: Command '['C:\\Users\\admin\\env\\Scripts\\python.exe', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
# It is strange for me because I'm using python for a long time and never had such a problem.Highest score (default)11
# On Ubuntu first, install the venv of the specific python version 
#? sudo apt install python3.10-venv
#? python3.10 -m venv a9env 
# # specify the python version. This will create the virtual env "myenv"
# !!! Sve se da! Samo treba traziti!
# Deaktiviranje jednostavno sa "deactivate". Ponovno aktiviranje je automatsko i uvjek uz automatsku odradu kde "source /home/antun/Documents/aCod/App9/a9env/bin/activate" kad podizemo novi terminal!!! ili rucno odradom te kde iz istog terminala. Ne treba nikakve popravke ala Mosh, start trokut radi sa pyinterpreterom iz virtenv-a!
#? /home/antun/Documents/aCod/App9/a9env/bin/python /home/antun/Documents/aCod/App9/272_SettingUpVirtualEnvironment.py
# Ard kaze da po zatvaranju i ponovnom ulasku u mapu projekta moramo zatvoriti pa otvoriti terminal, sto je dokazana istina!!