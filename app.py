from flask import Flask,jsonify,request,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' 
app.config['MYSQL_PASSWORD']='roottoor'
app.config['MYSQL_DB']='prathibha_cse'
mysql=MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/myname/<name>')
def myname(name):
    return jsonify({"message":"hello","name":name}) 


@app.route('/mydetails',methods=["get","post"])
def det():
    name=request.args.get("name")
    city=request.args.get("city")
    address=request.args.get("address")
    return f"{name} {city} {address}"

@app.route('/myhtml')
def myhtml():
    return render_template("home.html")

@app.route('/userDetail')
def userDetail():
    id=request.args.get("id")
    sql=f"SELECT * FROM user where id={id}"
    cur=mysql.connection.cursor()
    cur.execute(sql)
    results=cur.fetchall()
    print(results)
    cur.close()
    
    #id="18"
    #name="hgdt"
    #email="h@gmail.com"
    #password="adsfg"

    return render_template("user_detail.html",id=results[0][0],name=results[0][1],email=results[0][2],password=results[0][3])

@app.route('/getData')
def getData():
    id=request.args.get("id")
    sql=""
    if id is None:
        sql=f"SELECT * FROM user"
    else:
        sql="SELECT * FROM user where id={id}"
    cur=mysql.connection.cursor()
    cur.execute("SELECT*FROM user")
    results=cur.fetchall()
    cur.close()
    return jsonify(results)

@app.route('/register_save', methods=["GET", "post"])
def register_save():
    print(request.method)
    if( request.method )== "GET":
        return render_template("register.html")
    else:
        id=request.form.get("id")
        name=request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        cur = mysql.connection.cursor()
        sql = "INSERT INTO user(id,name,email, password) VALUES (%s, %s,%s,%s)"
        val = [id,name,email, password]
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return "register success"
@app.route('/getDataInHtml')
def getDataInHtml():
    id=request.args.get("id")
    sql=""
    if id is None:
        sql="SELECT * FROM user"
    else:
        sql=f"SELECT * FROM user where id={id}"
        
    cur=mysql.connection.cursor()
    cur.execute("SELECT*FROM user")
    results=cur.fetchall()
    cur.close()
    return render_template("userlist.html",userlist=results)


if __name__=='__main__':
    app.run()