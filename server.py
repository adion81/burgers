from flask import Flask,render_template,redirect,request

from mysqlconnection import connectToMySQL


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create',methods=['POST'])
def create():
    query = "INSERT INTO burgers (name,bun,meat,calories,topping_one,topping_two,created_at,updated_at) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,%(topping_one)s,%(topping_two)s,NOW(),NOW())"
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "topping_one": request.form['topping_one'],
        "topping_two": request.form['topping_two']
    }

    mysql = connectToMySQL('burgers')
    mysql.query_db(query,data)
    return redirect('/burgers')




@app.route('/burgers')
def burgers():
    query = "SELECT * FROM burgers;"
    burgers = connectToMySQL('burgers').query_db(query)
    print(burgers)
    return render_template("results.html",all_burgers=burgers)





if __name__=="__main__":
    app.run(debug=True)