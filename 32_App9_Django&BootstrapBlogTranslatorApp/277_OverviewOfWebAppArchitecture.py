# 9'07''
# Shematski prikaz app-a i najava da necemo nista kodirati, tj samo cemo pokusati razumjeti arhitekturu Django App-a
# diagram sa 8 slicica
# slicica 11 je shema app-a iz userova kuta: title content, content, autor, datum
# da bi user vidio 11 mi kao devepsi moramoraditi sa 12 tj html-templatesima koji imaju standarne <html>, <body> itd ali i ponesto specificno i djangovo tj {}-djangotagse unutar kog su i naslovi {title}, {content}, {author}, {date} itd
# specifikum djangotag-ova sluzi kako bi db-ovi u njih deliverali tj punili pa zato i imamo sljedecu komponentu django-appa tj 13-db.sqlite3 sa tablicom blog_post i poljima title, content, author, date, slug. Svaki red u toj tablici je jedan blog-post.
# 21-models definira db, tablicu, polja a preko html-tempsa i sucelje za usera. Ima class koji defa db-tablicu tj formu. Tu ne unosimo nikakve stvarne vrijednosti!
# 22-urls.py fajl vodi brigu o urls-rootingu: temelj rada ovog djela bazira se na polju slug db-ea koje je u svakom razrjesavanju url-ea na 2. mjestu: npr "example.com/<slug>" ako u polju slug nadje unos on kontaktira korespondnog "view"-a
# view.blog iz urls.py inicira 23-views.py koji onda brine o userovom zahtjevu i daje mu pravi odgovor u interface
# za svaki novi template iamo korespondnu tablicu iz db-ia sa odgovarajucim poljima koja bi nastala dodavanjem nove klase u models.py a u urls.py imali bi smo novi patern kao i novu klasu u views.py
# konacno 31-admindio koji moze posluziti i kao kontakt interface za kreatore bloga sa svim potrebnim poljim: title, content itd. Ima i drugih nacina popune bloga, npr 32-server koji skuplja date i popunjava tablice