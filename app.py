from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='roottoor'
app.config['MYSQL_DB']='project'
mysql=MySQL(app)
CORS(app)

@app.route('/')
def home():
    return 'job listing'
@app.route('/getjoblisting',methods=["GET"])
def getjob():
        sql="select * from job_listing"
        cur=mysql.connection.cursor()
        cur.execute(sql)
        results=cur.fetchall()
        cur.close()
        return jsonify(results)

@app.route('/postjoblisting',methods=["POST"])
def post():
        json=request.get_json()
        job_id=json.get("job_id")
        job_name=json.get("job_name")
        job_description=json.get("job_description")
        qualification=json.get("qualification")
        email=json.get("email")
        job_type=json.get("job_type")
        company_name=json.get("company_name")
        location=json.get("location")
        salary=json.get("salary")
        last_date=json.get("last_date")
        cur=mysql.connection.cursor()
        sql="insert into job_listing(job_id,job_name,job_description,qualification,email,job_type,company_name,location,salary,last_date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=[job_id,job_name,job_description,qualification,email,job_type,company_name,location,salary,last_date]
        cur.execute(sql,val)
        mysql.connection.commit() 
        cur.close()
        return "success"

@app.route('/searchjoblisting', methods=["GET"])
def search_job():
    data = request.get_json()  
    keyword = data.get("keyword") 
    cur = mysql.connection.cursor()
    sql = """SELECT * FROM job_listing 
             WHERE job_name LIKE %s 
                OR location LIKE %s 
                OR company_name LIKE %s"""
    val=(f"%{keyword}%",f"%{keyword}%",f"%{keyword}%")
    cur.execute(sql,val)
    results = cur.fetchall()
    cur.close()
    return jsonify(results)


    

if __name__=='__main__':
    app.run(host='192.168.20.83', port=5000)