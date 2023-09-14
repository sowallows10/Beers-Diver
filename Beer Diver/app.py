import os
from flask import (
     Flask, 
     request, 
     render_template)
from model import recommend

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def top():
    return render_template('top.html')

@app.route('/kibun1', methods=['GET'])
def kibun1():
    return render_template('kibun1.html')
    
@app.route('/kibun2', methods=['GET','POST'])
def kibun2():
    if request.method == "GET":
        return render_template('kibun2.html')
    elif request.method == "POST":
        favs = request.form.getlist("fav")
        data_str = ",".join(favs)
        name,imageurl,url = recommend(data_str)
        return render_template('kibun2.html', name=name,imageurl=imageurl,url=url)

@app.route('/seikaku1', methods=['GET'])
def seikaku1():
        return render_template('seikaku1.html')

@app.route('/seikaku2', methods=['GET','POST'])
def seikaku2():
    if request.method == "GET":
        return render_template('seikaku2.html')
    elif request.method == "POST":
        favs = request.form.getlist("fav")
        data_str = ",".join(favs)
        name,imageurl,url = recommend(data_str)
        return render_template('seikaku2.html', name=name,imageurl=imageurl,url=url)

if __name__ == "__main__":
    app.run(debug=True)