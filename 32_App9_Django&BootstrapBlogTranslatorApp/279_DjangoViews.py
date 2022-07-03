# 4'41''
# u models.py definiramo class Post tj db-tablicu koja ce popunjavati nas html-template (njegove django tj dinamicke tagove). view.py je odgovoran za prijenos podataka iz db-ea u html-temps.
# editiramo view.py: class BlogView:
                    #model = Post
                    #template_name = 'blog.html'
# Prije ubacivanja Post za model morali smo iz fajla models importati klasu Post (ali na malo cudan nacin sa .models)
# nakon edita provjera u termu sa
#? python manage.py runserver
# i dok ja nisam dobio nikakvu gresku on je "da template.dir is not defined" zbog cega ide u settings i  tamo importa os - sad vise ne znam jesam li to sam napravio ili je to improvement od vremena snimanja videa?!?!
# popravio je to importanjem i sad nakon odrade idemo na hompe page localhost:8000 i pokazuje da pokusaj kucanja dogs i slicno rezultira greskama jer nemamo nista u nasoj db. U sljedecem videu unosimo! preko db browsera radi testiranja, normalno cemo to unositi preko djanga.
