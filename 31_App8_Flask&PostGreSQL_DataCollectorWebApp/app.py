from flask import Flask, render_template, request
import flask


app=Flask(__name__)

# db=SQLAchemy(app)

# class Data


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(request.form)     # ImmutableMultiDict([('email_name', 'a@a.hr'), ('height_name', '175')])
        print(email, height)    # a@a.hr 175
        return render_template("success.html")

if __name__ == '__main__':
    app.debug=True
    app.run()      # port 5000 je def i nisam ga morao pisati ali kao podsjetnik gdje se mjenja