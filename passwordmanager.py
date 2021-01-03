import passs
import os
import time
uuu=passs.getuser()
ppp=passs.getpass()

username=uuu[0]
password=ppp[0]
print("--PASSWORD MANAGER--".center(71,"🔑"))  
print("^^^^^^^^^^^^^^^^^")
user=input("Enter your username     :: ")
pas=input("Enter your password     :: ")
print("^^^^^^^^^^^^^^^^^")
if username!= user or password != pas:
    print("")
    print("Incorrect username or password.")
    print("Retry in 5 seconds...*WARNING!!! ONLY ONE MORE CHANCE!!!!*")
    for i in range(1,6):
        print(i," >> ",end="")
        time.sleep(1)

    
    print("")
    print("")
    print("^^^^^^^^^^^^^^^^^")
    user=input("Enter your username     :: ")
    pas=input("Enter your password     :: ")
    print("^^^^^^^^^^^^^^^^^")
    print("")
    if username!= user or password != pas:
        print("")
        print("⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠")
        print("")
        print("Incorrect username or password.")
        print("No more chances , exiting in >>>>>>>>")
        for i in range(1,3):
            print(i," >> ",end="")
            time.sleep(1)

        print("⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠")
        print("")
        
        os.system("cls")
print("")
while user== username and pas==password:
      
    print("")
    print("🎇_______________________________________________MAIN MENU________________________________________________________________🎇")
    print("")
    print("🔐*************************************************************************************************************************🔐")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 1 👈-to ADD DETAILS >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 2 👈-to EDIT DETAILS >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 3 👈-to REMOVE DETAILS >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 4 👈-to VEIW ALL >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 5 👈-to AUTO GENERATE PASSWORD FOR OTHER USES >>>~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 6 👈-to SEARCH >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 7 👈-for APP SETTINGS >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 8 👈-to EXIT >>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("🔐*************************************************************************************************************************🔐")
    print("")
    
    option=int(input("Enter your option::"))
    
    
    if option==1:
        print("")
        print("⚙"*20)
        print("")
        print("-> a <- to ADD DETAILS.")
        print("-> b <- to ADD DETAIL WITH AUTO PASSWORD.")
        print("-> c <- to GO TO MAIN MENU.")
        print("")
        print("⚙"*20)
        print("")
        optionevent=input("Enter your option::")
        while True:
            

            if optionevent.lower() == "a":
                passs.adddata()
                break
            elif optionevent.lower() =="b":
                passs.autogen()
                break

            elif optionevent.lower() == "c":
                print("")
                print("<<<<<<<< Returning to main menu >>>>>>>>")
				#print("")
                break
            else:
                print("")
                print("Enter a valid option!!!")
                pirnt("")
                break

    elif option==2:
        if passs.total() == 0:
            print("")
            print("No details added yet!!")
            print("")
        else:
            
            print("")
            print("🛠"*20)
            print("")
            print("-> a <- to CHANGE PASSWORD.")
            print("-> b <- to CHANGE USERNAME.")
            print("-> c <- to CHANGE EMAIL LINKED.")
            print("-> d <- to RETURN TO MAIN MENU. ")
            print("")
            print("🛠"*20)
            print("")
            optioncar=input("Enter your option::  ")
            print("")
            while True:
                

                if optioncar.lower() == "a":
                    passs.changepass()  
                    break
                elif optioncar.lower() == "b":
                    passs.changeuser()
                    break
                elif optioncar.lower() == "c":
                    passs.changeemail()
                    break
                
                elif optioncar.lower() == "d":
                    print("")
                    print("<<<<<<<< Returning to main menu >>>>>>>>")
                    #print("")
                    break
                else:
                    print("")
                    print("Enter a valid option!!!")
                    print("")
                    break

    elif option==3:
        if passs.total() == 0:
            print("")
            print("No details added yet!!")
            print("")
        else:
            passs.removedetails()
        

    elif option==4:
        if passs.total() == 0:
            print("")
            print("No details added yet!!")
            print("")
        else:
            passs.display()
        
        

    elif option==5:
        print("⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠")
        print("")
        print("The password generated is ",passs.passwordgen())
        print("")
        print("⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠ ⚠")
        

    elif option==6:
        if passs.total() == 0:
            print("")
            print("No details added yet!!")
            print("")
        else:
            passs.search()

    elif option==7:
        while True:
            print("-> 1 <- to change master password ")
            print("-> 2 <- to change username.")
            print("-> 3 <- to exit.")
            print("")
            us=int(input("Your option is :: "))
            print("")
            if us==1:
                oldp=input("Enter your existing password :")
                if oldp == ppp[0]:
                    passs.mainpass()
                    
                    print("")
                    print("<<<< Password succesfully updated >>>>")
                    print("")
                else:
                    print("")
                    print("⚠⚠⚠⚠⚠ Old password does not match ⚠⚠⚠⚠⚠")
                    print("")
            
            elif us==2:
                
                print("")
                olda=input("Enter your existing username::")
                oldi=input("Enter your existing password::")
                
                if olda==uuu[0] and oldi==ppp[0]:
                    print("")
                    passs.mainuser()
                    
                    print("<<<< Username succesfully updated >>>>")
                    print("")
                else:
                    print("")
                    print("⚠⚠⚠⚠⚠ Old username or password does not match ⚠⚠⚠⚠⚠")
                    print("")

            else:
                print("")
                print("<<<<< Returning to main menu >>>>>")
                print("")
                break   

    elif option== 8:
        print("")
        print("We keep all your details safe,thank you!!!")
        print("")
        print("<<<<<<<< Exiting application in 5 >>>>>>>>")
        for i in range(1,6):
            print(i," >> ",end="")
            time.sleep(1)
        os.system("cls")		
                 
        break
    else:
        print("Enter a valid option!!!")
