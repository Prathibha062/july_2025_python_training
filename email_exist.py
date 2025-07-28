import mysql.connector
def checkemail(email1):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="prathibha_cse"

    )
    print(mydb)
    mycursor=mydb.cursor()
    sql="select*from user where email=%s"
    val=(email1,)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    
    if result:
        print("email already exists")
    else:
        print("email does not exist")
    mydb.commit()
    mycursor.close()
    mydb.close()
email1=input("enter the email to check:")
checkemail(email1)
    



    


