# 16'28''
# bootstrap koristi napisani css-kod i primjenjuje ga na class-e
# Dva su nacina koristenja BS-a, instalirati ga ili sa jsDelivery (nas izbor) sa stranice:"https://getbootstrap.com/docs/5.1/getting-started/introduction/"
# Prvo se na ciljnom html-u kreira head tag i u njega se kopira link: <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
# potom sljedi JS-fajl kojeg kopiramo iz odjeljka bundle neposredno prije zatvaranja body-taga: "<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>"
# save index i refresh app - odmah je doslo do poz promjena!
# Sada sljedi "StarterTemplate" iz kojeg Ardi uzima ponesto (ne sve!): lang -liniju, metatagse takodjer ispod head-taga, te titel liniju ispod prvog linka ispod head-taga i mjenja tekst sukladno nazivu naseg Appa.
# Inace kompletan kod tog djela:
#? <!doctype html>
#? <html lang="en">
#?   <head>
#?     <!-- Required meta tags -->
#?     <meta charset="utf-8">
#?     <meta name="viewport" content="width=device-width, initial-scale=1">
#? 
#?     <!-- Bootstrap CSS -->
#?     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" # i?ntegrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
#? 
#?     <title>Hello, world!</title>
#?   </head>
#?   <body>
#?     <h1>Hello, world!</h1>
#? 
#?     <!-- Optional JavaScript; choose one of the two! -->
#? 
#?     <!-- Option 1: Bootstrap Bundle with Popper -->
#?     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" # i?ntegrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
#? 
#?     <!-- Option 2: Separate Popper and Bootstrap JS -->
#?     <!--
#?     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/# I?qJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
#?     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" # i?ntegrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
#?     -->
#?   </body>
#? </html>

# Potom slijedi udivanje u div-tagove django-tagova naseg index-a
# dodavanje class="container" div tagu i refresanje i odmah se pomakao izbornik!
# zatim div-a svaki post unutar vec udivanog djela i indentaju se postovi a zadim doda clas="card m-3". Refresh donosi neku vrstu granica izmedju postova
# sljedi jos jedan div ispod div-a classCarda a okolo postova sa class="card-body"
# potom jos jedan div sa class="card-title" kojeg poslije ipak zamjeni sa <h2>
# potom ispod h2  jos jedan <div class="card-text"> sa {{post.content}}. Ovaj div, kao i h2 tag te postovi su svi sa istom indentacijom!
# Refresh i content je takodjer tu!
# malo rada na buttonu u sklopu a-taga. Smeta me sto je kod njega button taman a kod mene se to ne vidi, sve je bilo!
# iznad a-taga dodaje jos jedan div class="card-text" sa {{post.author}} a mice p-tag jer je dupliranje. Save F5 i ok!
# Na kraju sve divove na uvlaci a-taga mjenja u p-tag kao i h2 tagove oko teksta "Read more"
# U konacnici nemam obojan Read More! Nasao gresku! jedno slovo nisam utipkao!
