# 12'37''
# Syling Bootstrap-a samo smo primjenili na index page i druge stranice to ne osjecaju - npr about je totalno bez styling-a.
# Potom prelazi na naglasavanje nedostatka navigacije (skroz druga stvar ali ardo ardo) pa da i to treba realizirati - sve to u ovom videu!
# Sto se navigacije tice, jedan nacin bio bi da se navigacijski meni implementira na svakoj stranici koju imamo u html-u sto bi bilo krsenje DRY principa. Da to ne radimo pomaze nam tzv Template Inheritance TI. 
# Sustina TI je u pravljenju toga sto bi se ponavljalo u obliku jednog i posebnog fajla a potom njegovom povezivanju sa ostalim fajlovima-korisnicima.
# pravimo /templates/base.html  i pocinjemo sa <nav> tabom
# spustamo se do <a> taba i href-ova unutar kojih stavljamo vrijednosti za name iz path-ova urls.py fajla
# potom idemo u index i cut-amo sve od open-body-taga do vrha i ljepimo na vrh <nav> taga
# ponovo u index i cut odozdo od closing html-taga do scripte bootstrapa i ljepimo na kraj base.html-a
# navedenim operacijama base.html je postao parent a index.html  kao i druge stranice child koji od base dobivaju pocetak i kraj tj bootstrapiranje!
# da bi to realizirali do kraja treba index-u kao i svakoj drugoj stranici (na kojima takodjer prethodno trebamo obrisati body-tagove) signalizirati da se prosire na base.html. To radimo dodavajuci na početak django-tag: {%  extends 'base.html' %}
# potom idemo ponovo na base.html i ispod closing <nav> taga dodajemo: {%  block content %} i ispod {%  endblock content %} 
# Isto to cinimo na pocetak i na kraj svake stranice.
# Nakon F5 dobijamo 2 tocke. Da bi dobili tekst-link vracamo se u base.html i unutar <a> taga upisujemo nazive "Home" i "About Us". 
# Ako zelimo da nam sadrzaj About-a bude ljepsi smijemo dodati tag. Ard dodaje <div> i class: <div class="container">
# Na kraju najavljuje sljedeci video kao bavljenje stajlingom navigation-itemsa