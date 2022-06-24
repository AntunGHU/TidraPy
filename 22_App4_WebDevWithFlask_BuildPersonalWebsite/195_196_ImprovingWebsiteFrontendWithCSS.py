# 195 In the next lecture, we will add CSS styling to the webpage. Sometimes, when you make a change to the CSS file and reload the webpage, the changes are not shown because the browser uses the previous cached styling. If this happens, open the browser in private (incognito) mode and load the webpage there.

# 196:
# 6'00''
# Lekcija dodavanja some CSS-Styling-a: Treba napisat css-fajl pa ga staviti u mapu static/css/ te linkati sa ostatkom!
# U mapu static osim css-a idu i drugi sastojci, npr, ako imamo slike za web kreiramo u staticu mapu images i stavljamo ih u nju!
# linkovi iz layout-html-a na ostale html-djelove idu iz body-ia a na css i npr java script idu izvan body-a unutar head-taga.

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)