from datetime import datetime


name = "pradyumna"
password = "paddu97"
chances = 0

while True:
    user_name = input("Please Enter the user name:  ")
    if user_name== name:
        break
    else:
        print("Wrong user name please try again")
        chances =chances+1
        if chances==5:
            print("Sorry try again")
            quit()


while True:
    user_password = input("Please Enter the User Password:  ")
    if user_password == password:
        print("Welcome to My Store")
        break
    else:
        print("Wrong Password please try again")
        chances=chances+1
        if chances==5:
            print("Sorry try again")
            quit()

#store item names------------

store_items = """ 
spectrum Rs 500
pen box Rs 50
charts Rs 30
bag Rs 600
file Rs 199"""

#declaration--------------

price = 0
pricelist = []
total_price = 0
final_price = 0
ilist = []
qlist = []
plist = []

items = {"spectrum":500,"pen box":50,"charts":30,"bag":600,"file":199}
option = int(input("For List of Items PRESS 1:  "))

if option ==1:
    print(store_items)

    for i in range(len(items)):
        inp1 = int(input("If you want to buy PRESS 1 or 2 for EXISTS:  "))
        if inp1 == 2:
            break
        if inp1 == 1:
            item = input("Please Enter your Item name:  ")
            quantity = int(input("please Enter your quantity:  "))
            if item in items.keys():
                price = quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                total_price+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst = (total_price*5)/100
                final_amount = gst+total_price

            else:
                print("Sorry you enter ITEM IS NOT AVAILABLE")
        else:
            print("you enter Worng Number")
        
        inp = input("If you want bill enter yes or no:  ")
        if inp == "yes":
            pass
            if final_amount!=0:
                print(20*" ", "FRIENDLY BOOK STORE",20*" ")
                print(20*" ","Friends Colony",20*" ")
                print("Name:", name)
                print("Date:", datetime.now())
                print()
                print("Sno","Quantity","Price")
                for i in range(len(pricelist)):
                    print(i,ilist[i],qlist[i],plist[i])
                print()
                print("Total Amount:",20*" ", total_price)
                print("GST:",20*" ", gst)
                print("Final Amount:",5*" ", final_amount)
                print()
                print("THANKS FOR VISITING MY STORE")