import passs

username="jebin"
password="secret"
print("^^^^^^^^^^^^^^^^^")
user=input("Enter your username::  ")
pas=input("Enter your password::  ")
print("^^^^^^^^^^^^^^^^^")
print("")
while user== username and pas==password:
    print("--PASSWORD MANAGER--".center(61,"🔑"))    
    print("")
    print("________________________________________________________________________________MAIN MENU____________________________________________________________________________________")
    print("")
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    print("                     ENTER ~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 1 👈- to ADD DETAILS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 2 👈-to EDIT DETAILS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 3 👈-to REMOVE DETAILS>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 4 👈- to VEIW ALL>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 5 👈- to AUTO GENERATE PASSWORD FOR OTHER USES>>>~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 6 👈- to SEARCH>>>~~~~~~~")
    print("                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<-👉 7 👈-to EXIT>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
    print("")
    option=int(input("Enter your option::"))
    
    if option==1:
        print("")
        print("🏁"*20)
        print("")
        print("-> a <- to ADD DETAILS.")
        print("-> b <- to ADD DETAIL WITH AUTO PASSWORD.")
        print("-> c <- to GO TO MAIN MENU.")
        print("")
        print("🏁"*20)
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
                print("Returning to menu....")
                print("")
                break
            else:
                print("")
                print("Enter a valid option!!!")
                pirnt("")
                break

    elif option==2:
        print("")
        print("🏎"*20)
        print("")
        print("-> a <- to CHANGE PASSWORD.")
        print("-> b <- to CHANGE USERNAME.")
        print("-> c <- to CHANGE EMAIL LINKED.")
        print("-> d <- to RETURN TO MAIN MENU. ")
        print("")
        print("🏎"*20)
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
                print("Returning to menu....")
                print("")
                break
            else:
                print("")
                print("Enter a valid option!!!")
                print("")
                break

    elif option==3:
        passs.removedetails()
        

    elif option==4:
        passs.display()
        

    elif option==5:
        print("The password generated is ",passs.passwordgen())
        

    elif option==6:
        passs.search()
        

    elif option== 7:
        print("")
        print("We keep all your details safe,thank you")
        break
    else:
        print("Enter a valid option!!!")
        break
