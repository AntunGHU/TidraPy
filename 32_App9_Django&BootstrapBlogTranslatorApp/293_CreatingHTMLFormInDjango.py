# 7'45'' 
# Kreiramo stranicu sa dva polja i buttonima ispod - pitanje promisljanja dizajna
# kreiramo i editamo u mapi /templates/translator.html
# umjesto da html-a ard samo pasta ranije pripremljen kod
# rekao da ce kod zakaciti u lekciji ali morao sam puno znati (inspect elements, sources itd) da do njega dodjem i voila sa svim prosirenjima koja ce naknadno doci:
#? {% extends 'base.html' %}
#? {% block content %}
#? <div class="container">
#?     <form action="{% url 'translator_view' %}" method="post">
#?         {% csrf_token %}
#?         <div class="row">
#?             <div class="col-sm-6 mt-3 left">
#?                 <textarea class="form-control" rows="3" name="my_textarea">{{original_text}}</textarea>
#?             </div>
#?             <div class="col-sm-6 mt-3 left">
#?                 <textarea class="form-control" rows="3">{{output_text}}</textarea>
#?                 <input class="btn btn-primary ml-3 mt-3" type="submit" value="Submit">
#?             </div>
#?         </div>
#?     </form>
#? </div>
#? {% endblock content %}
# na zalost, vec sam sve ukucao! pa sad samo mogu kao ardit pokusati vidjeti u browseru - i cini mi se da nam je sve isto - pravilno sam sve prepisao
# napominje da link prema bootstrapu nije za stalno potreban jer je on vec u base.html-eu, pa ga brise te dodaje django tagove linkove prema base.html