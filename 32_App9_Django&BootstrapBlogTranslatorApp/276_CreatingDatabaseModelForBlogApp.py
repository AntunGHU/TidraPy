# 12'23''
# Dodavat cemo kod u nas fajl /blog/models.py
#? class Post(models.Model):
# nakon popunjavanja class Post-a ubacuje import za jedan podatak iz druge db-tablice
#? from django.contrib.auth.models import User
# on_delete=models.CASCADE u jednom polju znaci da ce nesto brisano kaskadno brisati i drugo polje
# status nosi adminmogucnosti objave bloga ili snimanja nedovrsenog draft-a ili nacrta
# nakon snimanja dosad unesenog trebamo apply-ati na db izvodeci 2 k-de:
#? python manage.py makemigrations
#? python manage.py migrate
#! vec poslije pokusaja prve greska: ModuleNotFoundError: No module named 'tkinter'
# potrazio i nasao: 
# # 👇️ === UBUNTU / DEBIAN ===
#? sudo apt-get install python3-tk
# 🚨 Make sure to specify correct Python version.
# For example, my Python 3.10, so I would install as
#? sudo apt-get install python3.10-tk
# i rjeseno!!! ponovo izvodim prvu k-du i sad je sve ok!!, drugu i ok!!
# sad Ardit pokazuje na svom db-vieweru da su sva definirana polja kao i sama tablica blog kreirani!!!
# pokusavao otvoriti basu sa pgAdmin4 i slucajno uspio doci do "DB Browser for SQLite" takoda sad mogu i ja!!!

