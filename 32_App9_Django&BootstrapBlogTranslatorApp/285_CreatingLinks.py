# 5'44''
# Kreiranje linkova moguce  je koristenjem <a> tagova umjesto h2 ili p i stavljanjem "localhost" u href=... Medjutim tada kad se app deploy-a i dobije svoju adresu to vise nece raditi.
# zato u a-tad za href stavljamo {}-tagove:" <a href="{% url 'blog_view' %}">{{post.title}}</a> "
# snimamo i proba - radi!!!
# Kao final touch ponovo stavlja h2 tagove:"<a href="{% url 'blog_view' post.slug %}"><h2>{{post.title}}</h2></a>"