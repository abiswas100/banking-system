import mysql.connector as m
class account:
    def newaccount(self):
        name=input("Enter account holder's name")
        acc_no = int(input("enter account number"))        
        amt=int(input("Enter amount"))      
        mydb = m.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bank"
         )
        mycursor = mydb.cursor()
        sql = "INSERT INTO accounts (User_name, Account_number,Initial_deposit,Balance) VALUES (%s, %s, %s,%s)"
        val = (name,acc_no,amt,amt)
        mycursor.execute(sql, val)
        mydb.commit() 
        print(mycursor.rowcount, "record inserted.")
        mydb.close()


    def deposit(self):
        mydb = m.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bank"
        )
        mycursor = mydb.cursor()
        
        ##data fetch
        
        acc_no = int(input("enter the account number"))
        sql = "SELECT * FROM accounts WHERE (Account_number=%s)"
        val = (acc_no,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchone() # return a tuple
        name,number,inital,balance = myresult
        balance =int(balance)
        print("the balance for",name,"is",balance)
        print(type(balance))
        # data manipulation        
        
        deposit = int(input("Enter deposit amount"))
        balance = balance + deposit
        sql="UPDATE accounts SET Balance = %s WHERE Account_number=%s"
        val=(balance,acc_no)
        mycursor.execute(sql, val)
        
        mydb.commit()
        mydb.close()


    def withdraw(self):
        mydb = m.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bank"
        )
        mycursor = mydb.cursor()

        ##data fetch
        
        acc_no = int(input("enter the account number"))
        sql = "SELECT * FROM accounts WHERE (Account_number = %s)"
        val = (acc_no,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchone()
        name,number,balance = myresult
        
        print("the balance for",name,"is",balance)
        
        # data manipulation        
        
        withdrawl = int(input("Enter withdrawl amount"))
        balance = balance - withdrawl
        sql="UPDATE accounts SET Balance = %s WHERE Account_number=%s"
        val=(balance,acc_no)
        mycursor.execute(sql, val)
        
        mydb.commit()
        mydb.close()
    
    def fetch(self):
        mydb = m.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bank"
        )
        mycursor = mydb.cursor()

        ##data fetch
        
        acc_no = int(input("enter the account number"))
        sql = "SELECT * FROM accounts WHERE (Account_number = %s)"
        val = (acc_no,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchone()
        name,number,balance = myresult
        
        print("the balance for",name,"is",balance)
        


obj=account()
while 1:        
        ch=int(input("Enter choice  1 for new account... 2 for transactions... 3 for exit ..."))
        if ch==1:obj.newaccount()
        elif ch==2:
            print("1.for deposit\n2.for withdraw\n3.for balance info")
            f=int(input("\n Enter choice "))
            if f==1 : obj.deposit()
            elif f==2 :obj.withdraw()
            elif f==3 :obj.fetch()
        else:exit()
