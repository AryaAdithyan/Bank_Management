#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as sc
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def begin():
    mydb= sc.connect(host="localhost",user="root", password="DfsSat$123")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE ND11")

    mycursor.execute("USE ND11")
    mycursor.execute("CREATE TABLE bank (account_number INT PRIMARY KEY, user_name VARCHAR(50), branch_name VARCHAR(50), account_type VARCHAR(50), starting_balance DECIMAL")
    mydb.commit()


# In[3]:


def accountcreation():
    print("\n\n\n")
    print("WELCOME TO INDIAN BANK")
    print("######################")
    print("HAPPY TO KNOW THAT YOU ARE STARTING ACCOUNT HERE")
    print("ENTER USER DETAILS")
    print("#############################")
    b_accno=input("Enter Account No:")
    b_name=input("Enter USer name :")
    b_bname=input("Enter branch name:")
    b_type=input("Enter Type of Account:")
    b_amount=int(input("Enter starting balance:"))
    conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
    mycursor=conn.cursor()
    query1="insert into bank values('{}','{}','{}','{}',{})".format(b_accno,b_name,b_bname,b_type,b_amount)
    mycursor.execute(query1)
    conn.commit()
    conn.close()
    print("SUCCESSFUULY CREATE NEW ACCOUNT !!!!")
    


# In[4]:


def homepage():
    print("\n\n\n")
    print("####################################################")
    print("WELCOME TO INDIAN BANK ")
    print("####################################################")
    print("HOME PAGE MENU")
    print("1. USER ACCOUNT CREATION")
    print("2. UPDATE ACCOUNT DETAILS")
    print("3. TRANSACTIONS")
    print("4. SEARCH DETAILS")
    print("5. REMOVE USER DETAILS")
    
    print("###################################################")
    op=int(input("Enter your option"))
    if op==1:
        accountcreation()
    elif op==2:
        updatedetails()
    elif op==3:
        transaction()
    elif op==4:
        search()
    elif op==5:
        remove()
    else:
        print("Invalid option")


# In[5]:


def login():
    print("\n\n\n")
    print("##############################################")
    print("WELCOME TO INDIAN BANK LOGIN SECTION")
    print("#################################################")
    user=input("Enter your user ID :")
    pas=input("Enter your password:")
    if user=="Nandhana" and pas=="DfsSat$123":
        print("############################")
        print("SUCCESSFULLY LOGGED!!!!!")
        homepage()
    else:
        print("INCORRECT CREDENTIALS")
        login()


# In[6]:


def updatedetails():
    u_accno=input("Enter the account number of the user we want to update ")
    u_name=input("Enter correct name:")
    u_bname=input("Enter correct branch name :")
    u_type=input("Enter correct type of account")
    u_amount=int(input("Enter correct amount:"))
    conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
    mycursor=conn.cursor()
    query1="update bank set user_name='{}',branch_name='{}',account_type='{}',starting_balance={} where account_number='{}'".format(u_name,u_bname,u_type,u_amount,u_accno)
    mycursor.execute(query1)
    conn.commit()
    conn.close()
    print("SUCCESSFUULY UPDATE  ACCOUNT DETAILS !!!!")
    


# In[7]:


def transaction():
    print("\n\n\n")
    print("######################################")
    print("WELCOME TO INDIAN BANK")
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. BALANCE ENQUIRY")
    print("4. GO TO MAIN PAGE")
    op=int(input("Enter your option:"))
    if op==1:
        d_accno=input("Enter you account number:")
        d_amount=int(input("Enter the amount you want to deposit:"))
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        query1="update bank set starting_balance =starting_balance+{} where account_number ='{}'".format(d_amount,d_accno)
        mycursor.execute(query1)
        conn.commit()
        conn.close()
        print("SUCCESSFUULY CREDIT THE AMOUNT TO YOUR   ACCOUNT  !!!!")
    elif op==2:
        d_accno=input("Enter you account number:")
        d_amount=int(input("Enter the amount you want to withdraw:"))
        conn=sc.connect(host="localhost",user="root",password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        query1="update bank set starting_balance=starting_balance-{} where account_number='{}'".format(d_amount,d_accno)
        mycursor.execute(query1)
        conn.commit()
        conn.close()
        print("SUCCESSFUULY WITHDRAW THE AMOUNT FROM  YOUR   ACCOUNT  !!!!")
    elif op==3:
        u_accno=input("Enter the account number of the user we want to search:")
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        query1="select account_number,user_name,starting_balance from bank where account_number='{}'".format(u_accno)
        mycursor.execute(query1)
        myrecord=mycursor.fetchall()
        for x in myrecord:
            print(x)
        conn.close()
        print("SUCCESSFUULY DISPLAY THE BALANCE  DETAILS !!!!")
    elif op==4:
        homepage()
    else:
        print("INVALID OPTION")
    


# In[8]:


def search():
    u_accno=input("Enter the account number of the user we want to search")
    conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
    mycursor=conn.cursor()
    query1="select * from bank where account_number ='{}'".format(u_accno)
    mycursor.execute(query1)
    myrecord=mycursor.fetchall()
    for x in myrecord:  
        print(x)                    
    conn.close()
    print("SUCCESSFUULY DISPLAY THE ACCOUNT DETAILS !!!!")
    


# In[9]:


def remove():
    u_accno=input("Enter the account number of the user we want to remove")
    conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
    mycursor=conn.cursor()
    query1="delete from bank where account_number='{}'".format(u_accno)
    mycursor.execute(query1)
    conn.commit()
    conn.close()
    print("SUCCESSFUULY REMOVE THE ACCOUNT DETAILS !!!!")   


# In[10]:


def report():
    print("\n\n\n")
    print("#######################################")
    print("WELCOME TO INDIAN BANK ")
    print("#######################################")
    print("REPORT SECTION ")
    print("1. REPORT BASED ON TYPE OF ACCOUNT")
    print("2. REPORT BASED ON AMOUNT DEPOSITED")
    print("3. REPORT BASED ON LOCATION")
    print("4. GO TO HOME PAGE")
    op=int(input("Enter your option:"))
    if op==1:

        print("\n\n\n\n")
        print("##########################")
        print("WELCOME TO INDIAN BANK ")
        print("REPORT SECTION")
        nlist=[]
        xar=np.arange(1,5)
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        type1="Saving"
        type2="Current"
        type3="Business"
        type4="Loan"
        query1="select count(*) from bank where account_type='{}'".format(type1)
        query2="select count(*) from bank where account_type='{}'".format(type2)
        query3="select count(*) from bank where account_type='{}'".format(type3)
        query4="select count(*) from bank where account_type='{}'".format(type4)
        mycursor.execute(query1)
        myrecord1=mycursor.fetchall()
        conn.close()
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        mycursor.execute(query2)
        myrecord2=mycursor.fetchall()
        conn.close()
        
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        mycursor.execute(query3)
        myrecord3=mycursor.fetchall()
        conn.close()
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        mycursor.execute(query4)
        myrecord4=mycursor.fetchall()
        conn.close()
        for x in myrecord1:
            nlist.append(x[0])
        for x in myrecord2:
            nlist.append(x[0])
        for x in myrecord3:
            nlist.append(x[0])
        for x in myrecord4:
            nlist.append(x[0])
        print(nlist)
        plt.bar(xar,nlist,width=0.5,color=["red","green","blue","yellow"])
        plt.xlabel("Type of account")
        plt.ylabel("No of account holders")
        plt.title("BAR GRAPH ON TYPE OF ACCOUNT ANALYSIS")
        xnames=["Saving","Current","Business","Loan"]
        plt.xticks(xar,xnames,rotation=30)
    elif op==2:
        print("\n\n\n\n")
        print("##########################")
        print("WELCOME TO INDIAN BANK ")
        print("REPORT SECTION BASED ON AMOUNT DEPOSITED")
        nlist=[]
        xar=np.arange(1,5)
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        query1="select count(*) from bank where  starting_balance <500"
        query2="select count(*) from bank where  starting_balance >=500 and  starting_balance <=50000"
        query3="select count(*) from bank where  starting_balance >50000 and  starting_balance <=100000"
        query4="select count(*) from bank where  starting_balance >100000"
        mycursor.execute(query1)
        myrecord1=mycursor.fetchall()
        conn.close()
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        mycursor.execute(query2)
        myrecord2=mycursor.fetchall()
        conn.close()
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        mycursor.execute(query3)
        myrecord3=mycursor.fetchall()
        conn.close()
        conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
        mycursor=conn.cursor()
        mycursor.execute(query4)
        myrecord4=mycursor.fetchall()
        conn.close()
        for x in myrecord1:
            nlist.append(x[0])
        for x in myrecord2:
            nlist.append(x[0])
        for x in myrecord3:
            nlist.append(x[0])
        for x in myrecord4:
            nlist.append(x[0])
        print(nlist)
        plt.bar(xar,nlist,width=0.5,color=["red","green","blue","yellow"])
        plt.xlabel("AMOUNT RANGE ")
        plt.ylabel("No of account holders")
        plt.title("BAR GRAPH ON AMOUNT DEPOSITED ANALYSIS")
        xnames=["<500","500-50000","50000-100000",">100000"]
        plt.xticks(xar,xnames,rotation=30)
    	    
    elif op==4:
        homepage()
    else:
        print("INVALID OPTION")    


# In[2]:


conn=sc.connect(host="localhost",user="root", password="DfsSat$123",database="ND11")
mycursor=conn.cursor()
mycursor.execute("SELECT * FROM bank")
rows = mycursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the database connection
conn.close()


# In[ ]:




