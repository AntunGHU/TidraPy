# 7'32''
# Home nemamo ni u html-u. Ardi malo diskurira kojim redom i zakljucuje da pocnemo misljenjem o user-u, sucelju i seitu kojeg treba vidjeti, view-u koji treba povezati sucelje tj html-template sa Modelom tj db-eom. Znaci, od FE ka BE!
# kreiramo /templates/index.html (standard za naziv homepagea)
# edit index.html-a do django-tagova kad prekida i nastavlja unosenjem infoe u /blog/urls.py i dodajemo novi path u "urlpatterns = [
#    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
#    path('', views.HomeView.as_view(), name='home_view')  ] " 
# Nakon patha idemo kreirati view u views.py stvaranjem nove classe HomeView (koja moze bez metoda)
# Sve snimamo i osvezavamo i na "http://127.0.0.1:8000/" pojavljuje se tekst "This is home page!!"
# Za kraj Ardit istice razliku DetailedView(dobavlja datas from moduls i daje ih url-templateu) i TemplatedView (koja samo rendera template i ne dobavlja nikakve podatne iz main-modula)