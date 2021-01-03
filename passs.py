import mysql.connector
import random
import tabulate

from tabulate import tabulate
conn=mysql.connector.connect(host='localhost',user='root',passwd='123',charset="utf8")
cur=conn.cursor()
cur.execute("create database if not exists project")
cur.execute("use project")

cur.execute("create table if not exists passwords (NO int  primary key not null auto_increment,Username  varchar(240) not null ,Password varchar(240),Email_linked varchar(240),App_name varchar(240))")
cur.execute("alter table passwords auto_increment=100")
conn.commit()

cur.execute("create table if not exists user (NO int  primary key not null auto_increment,Username  varchar(240) not null ,Password varchar(240))")


cur.execute("alter table user auto_increment=50")
conn.commit()
c="insert into user (Username,Password)\
values('{}','{}')".format("jebin","secret")
cur.execute(c)
conn.commit()

def adddata():
	
	while True:
		print("* press enter to skip any field execept Username *")
		print("")
		username=input("Enter the  username           :")
		password=input("The password assigned         :")
		email=input("The Email address linked      :")
		app=input("The app name                  :")
			
		c="insert into passwords (Username,Password,Email_linked,App_name)\
		values('{}','{}','{}','{}')".format(username,password,email,app)
		cur.execute(c)
		conn.commit()
		print("")
		print("Data added succesfully!!!!")
		print("-----👉👉👉 1 to add more  👈👈👈-------👉👉👉 2 to leave 👈👈👈------")
		print("")
		op=int(input("Enter your option:  "))
		print("")
		if op==2:
			print("<<<<<<<< Returning to main menu >>>>>>>>")
			break    

def autogen():
	while True:
		print("")
		print("* press enter to skip any field execept Username *")
		print("")
		username=input("Enter the  username           :")
		password=passwordgen()
		email=input("The Email address linked      :")
		app=input("The app name                  :")
			
		c="insert into passwords (Username,Password,Email_linked,App_name)\
		values('{}','{}','{}','{}')".format(username,password,email,app)
		cur.execute(c)
		conn.commit()
		print("")
		print("Password generated=",password)
		print("Data added succesfully!!!!")
		print("-----👉👉👉 1 to add more  👈👈👈-------👉👉👉 2 to leave 👈👈👈------")
		print("")
		op=int(input("Enter your option:  "))
		print("")
		if op==2:
			print("<<<<<<<< Returning to main menu >>>>>>>>")
			break    

def passwordgen():
	low="abcdefghijklmnopqrstuvwxyz"
	upp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	num="0123456789"
	sym="!@#$%^&*"

	all=low+upp+num+sym
	print(">>>>>::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<<<<<")
	length=int(input("Enter the length of password *for safety use atleast 8 characters* ::"))
	print(">>>>>::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<<<<<")
	password="".join(random.sample(all,length))
	return password



def search():
		
	d=input("Enter the name of app  to be searched:  ")
	cur.execute("select * from passwords where App_name like '{}' ".format(d))
	r=[]
	for i in cur:
		r.append(i)
	h=['NO','Username','Password','Email_linked','App_name']
	print("")
	
	print(tabulate(r,headers=h,tablefmt="grid"))
	print("")
	print("<<<<<<<< Returning to main menu >>>>>>>>")
	print("")

def removedetails():
	display()
	print("")
	f=int(input("Enter the NO                      :"))
	d=input("Enter the app name to be deleted  :")
	print("")
	op=input("Sure you want to remove ?(y/n)    :")
	print("")
	while True:
			
		if op=="y":
			cur.execute("delete from passwords where App_name='{}' and NO={}".format(d,f))
			conn.commit()
			print("")
			print("Data Remmoved!!!")
			print("")
			print("<<<<<<<< Returning to main menu >>>>>>>>")
			print("")
			break
		else:
			print("Process aborted!!!! ")
			print("")
			print("<<<<<<<< Returning to main menu >>>>>>>>")
			print("")
			break

def changepass():
	display()
	print("")
	f=int(input("Enter the NO               :"))
	d=input("Enter the App_name         :")
	print("")
	pos=input('Enter the new password     :')
	cur.execute("update passwords set Password='{}' where App_name='{}' and NO={}".format(pos,d,f))
	conn.commit()
	print("")
	print("Password changed to ",pos," !!!")
	print("")
	print("<<<<<<<< Returning to main menu >>>>>>>>")
	print("")

def changeuser():
	display()
	f=int(input("Enter the NO               :"))
	d=input("Enter the App_name         :  ")
	print("")
	pos=input('Enter the new Username     :  ')
	cur.execute("update passwords set Username='{}' where App_name='{}' and NO={}".format(pos,d,f))
	conn.commit()
	print("")
	print("Username changed to ",pos," !!!")
	print("")
	print("<<<<<<<< Returning to main menu >>>>>>>>")
	print("")

def changeemail():
	display()
	f=int(input("Enter the NO               :"))
	d=input("Enter the App_name         :")
	print("")
	
	pos=input('Enter the new Email_linked :  ')
	cur.execute("update passwords set Email_linked='{}' where App_name='{}' and NO={}".format(pos,d,f))
	conn.commit()
	print("")
	print("Email_linked changed to ",pos," !!!")
	print("")
	print("<<<<<<<< Returning to main menu >>>>>>>>")
	print("")
	

def display():
	cur.execute("select * from passwords")
	r=[]
	for i in cur:
		r.append(i)
	h=['NO','Username','Password','Email_linked','App_name']
	print("")
	print(tabulate(r,headers=h,tablefmt="grid"))
	print("")
	
	print("")

def total():
	cur.execute("select * from passwords")
	r=[]
	for i in cur:
		r.append(i)
	return len(r)

def mainuser():
	pos=input('Enter the new master Username:')
	cur.execute("update user set Username='{}' ".format(pos))
	conn.commit()
	print("")
	print("Master username changed to ",pos," !!!")
	print("")
	print("<<<<<<<< Returning to main menu >>>>>>>>")
	print("")

def mainpass():
	pos=input('Enter the new password       :')
	cur.execute("update user set Password='{}'".format(pos))
	conn.commit()
	print("")
	print("Master password changed to ",pos," !!!")
	print("")
	print("<<<<<<<< Returning to main menu >>>>>>>>")
	print("")

def getpass():
	cur.execute("select Password from user")
	x= cur.fetchall()
	return x[0]
	

def getuser():
	cur.execute("select Username from user")
	x= cur.fetchall()
	return x[0]

