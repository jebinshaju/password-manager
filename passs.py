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
def adddata():
    
        while True:
                print("* press enter to skip any field execept Username *")
                print("")
                username=input("Enter the  username           :")
                password=input("The password assigned      :")
                email=input("The Email address linked   :")
                app=input("The app name                   :")
                 
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
                    break    

def autogen():
        while True:
                print("")
                print("* press enter to skip any field execept Username *")
                print("")
                username=input("Enter the  username           :")
                password=passwordgen()
                email=input("The Email address linked   :")
                app=input("The app name                    :")
                 
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
                    break    

def passwordgen():
        MAX_LEN = 12
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
						'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
						'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
						'Z'] 

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
			'*', '(', ')', '<&# 039;'] 

        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 

	# randomly select at least one character from each character set above 
        rand_digit = random.choice(DIGITS) 
        rand_upper = random.choice(UPCASE_CHARACTERS) 
        rand_lower = random.choice(LOCASE_CHARACTERS) 
        rand_symbol = random.choice(SYMBOLS) 

        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol +  random.choice(DIGITS) + random.choice(UPCASE_CHARACTERS)+random.choice(SYMBOLS)+random.choice(LOCASE_CHARACTERS) 
        return temp_pass


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

def removedetails():
        print("")
        f=int(input("Enter the NO                                   :"))
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
                        break
                else:
                        print("Process aborted!!!! ")
                        print("")
                        break

def changepass():
        display()
        print("")
        f=int(input("Enter the NO               :"))
        d=input("Enter the App_name     :")
        print("")
        pos=input('Enter the new password:  ')
        cur.execute("update passwords set Password='{}' where App_name='{}' and NO={}".format(pos,d,f))
        conn.commit()
        print("")
        print("Password changed to ",pos," !!!")
        print("")

def changeuser():
        display()
        f=int(input("Enter the NO               :"))
        d=input("Enter the App_name:  ")
        print("")
        pos=input('Enter the new Username:  ')
        cur.execute("update passwords set Username='{}' where App_name='{}' and NO={}".format(pos,d,f))
        conn.commit()
        print("")
        print("Username changed to ",pos," !!!")
        print("")

def changeemail():
        display()
        f=int(input("Enter the NO               :"))
        d=input("Enter the App_name:  ")
        print("")
        
        pos=input('Enter the new Email_linked:  ')
        cur.execute("update passwords set Email_linked='{}' where App_name='{}' and NO={}".format(pos,d,f))
        conn.commit()
        print("")
        print("Email_linked changed to ",pos," !!!")
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
