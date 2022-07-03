# 8'51''
# ponavlja da smo vec kreirali superusera ali idaje ponovo k-u "python manage.py createsuperuser"
# prijavljujemo se na admin interface sa userpass - posto sam dao operi ovlasti pamcenja ulazim direktno  
# editiramo /blog/admin.py
# importamo: "from .models import Post"
# registriramo: "admin.site.register(Post)" i save-amo i provjeravamo na stranici admin i nova grupa BLOG u django administarciji se stvorila!!! a clan joj je Posts! Kad kliknemo na Add pokraj otvara se forma koju smo na samom startu definirali i koja omogucava unos u db! Save! i ponovo u brovser i 8000/cats daje nas unos!!!
# problem u pregledu postova je sto se iz njihova naziva ne vidi cime se bave, svi imaju isto ime "Post object" Da bi sebi olaksali moramo tu ubaciti ime teme sto nas dovodi do price o dunder metodu  __str__ kojeg cemo dodati class-i Post u models.py. Nakon toga refreshamo admin-page i nazivi blogova se mjenjaju!!!
# Ako u spisku blogova osim  promjene naziva zelimo dodati jos poneki sadrzaj idemo u "blog/admin.py" i kreiramo novu klasu "class PostAdmin(admin.ModelAdmin):" te ju prijavljujemo pokraj Post klase u redu ispod:"admin.site.register(Post, PostAdmin)"
# Save-amo i reloadamo i pojavio se autor i vrijeme ali nestao title!? Popravak je lagan: samo smo jos dodali title uz vrijeme i author: "list_display= ('title', 'date_created', 'author')"

