import mysql.connector
def deletedata(id):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="prathibha_cse"
    )
    mycursor=mydb.cursor()
    sql="DELETE from user where id=%s"
    val=(id,)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record deleted")
id=input("enter id:")
deletedata(id)