name = "pradyumna"
password = "paddu@97"
pin = 1997
balance = 97000
debit = 0
chances= 0

user_name = input("Please Enter the User Name:  ")
user_password = input("Please Enter the User Password:  ")
if user_name == name and user_password == password:
    print(20*"_","Welcome to your Account",20*"_")
else:
    print("Please Enter the Valid details")



while True:
    user_pin = int(input("Please Enter the user pin:  "))
    if user_pin== pin:
        
        option = input("Choose the saving or balance enquiry: ")
        if option=="saving":
            withdraw = int(input("Enter your withdraw Amount: "))
            if withdraw<2000:
                current_balance = balance-withdraw
                print("Current balance is: ", current_balance)
                print(20*"_","Thank you",20*"_")
                break
            else:
                print("The amount should be less than 10001")
        elif option=="balance enquire":
            print("The Acutal balance is :",balance)
            print(20*"_","Thank you",20*"_")

            break
        
    else:
        print("Wrong user pin please try again")
        chances =chances+1
        if chances==5:
            print("Sorry try again")
            quit()
