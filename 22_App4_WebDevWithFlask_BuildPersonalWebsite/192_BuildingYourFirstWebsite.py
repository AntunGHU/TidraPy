# 8'07''
# Flask je Py-framework which have all tools to build Web Sites with Py

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "HomePage By Antisa!"

@app.route('/about/')
def about():
    return "About Website! Content goes here! By Antisa!"

if __name__=="__main__":
    app.run(debug=True)