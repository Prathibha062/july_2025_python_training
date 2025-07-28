import mysql.connector
def updatedata(id,name):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="prathibha_cse"
    )
    mycursor=mydb.cursor()
    sql="UPDATE user set name=%s where id=%s"
    val=(id,name)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record updated")
id=input("enter id:")
name=input("enter name:")
updatedata(id,name)