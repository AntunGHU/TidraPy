# 8'03''
# pocinje s isticanjem class Post u models.py i ponavljanjem da ona odredjuje db-tablicu, polja a preko njih i HTML-template
# HTML-tempse treba tek kreirati - to cinimo kreiranjem foldera "templates" u root-projekta, provjera sa ls
# potom unutar mape templates kreiramo "blog.html" i krecemo sa editiranjem. Brze provjer s dk i u exploreu pa 2x da otvori u browseru - zelio je istaci da klasicni h1 i html bi dali staticni tekst. Ali mi zelimo da se on mjenja prema kliku usera. Dinamicnost ostizemo djang-tagovima {{}}.
# nakon popunjenih par django-tagova provjera klasicnim browserom pokazuje doslovno te tagove "{{object.title}}" jer nismo stranicu povezali sa models.py
# povezivanje html-tempsa i stranice ide kroz "view" modul (sljedeci video) ali prije toga moramo reci nasim "mysite/settings.py"-ima gdje je nas template-url lociran

# edit setingsa: idemo na kraj fajla i upisujemo "TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')". Da smo stavili template unutar neke podmape morali bi i nju navesti npr 'templates/podmapa'. BASE_DIR je varijabla deklarirana na vrhu i to je root-dir.