from datetime import datetime

name = input("Enter your Name:")

lists = """
********************
wheat Rs 30/KG
Rice  Rs 50/KG
oil Rs 150/Ltr
Sugar Rs 40/KG
paneer Rs 100/KG
********************
"""

price = 0
pricelist = []
totalprice = 0
ilist = []
qlist = []
plist = []

items = {
    'wheat': 30,
    'Rice': 50,
    'oil': 150,
    'Sugar': 40,
    'paneer': 100
}

options = int(input("\nEnter 1 to see the menu or enter 2 to exit:"))

if options == 1:
    print(lists)
    while True:
        inp1 = int(input("\nIf you want to buy, press 1, or enter 2 to exit: "))
        
        if inp1 == 2:
            print("Thanks for your visit!")
            break
        elif inp1 == 1:
            item = input("\nEnter your items: ")
            Quantity = int(input("Enter Quantity in Kgs: "))
            
            if item in items:
                price = Quantity * items[item]
                pricelist.append((item, Quantity, price))
                ilist.append(item)
                qlist.append(Quantity)
                totalprice += price
                plist.append(price)
                GST = totalprice * 0.05
                Finalamount = totalprice + GST
            else:
                print("You entered a wrong item")
                continue
            
            inp = input("\nDo you want a bill? Enter 'yes' or 'no': ")
            
            if inp.lower() == "yes":
                print(40*'=', "Trend Supermarket", 40*'=')
                print(45*'=', "Hyderabad", 45*'=')
                print(name, 60*" ", "Date:", datetime.now())
                print(100*"-")
                print("S.No", 3*"\t", "Items", 4*"Quantity", 3*"\t", "Price")
                for j in range(len(ilist)):
                    print(j, 3*"\t", ilist[j], 4*"\t", qlist[j], 3*"\t", plist[j])
                print(100*"-")
                print(9*"\t", "Total Amount:", totalprice)
                print(9*"\t", "GST: ", 2*"\t", GST)
                print(100*"-")
                print(9*"\t", "Final Amount:", Finalamount)
                print(100*"-")
                print(40*"", "Thanks for Shopping")
                print(100*"-")
                print()
            elif inp.lower() == "no":
                pass
            else:
                print("You have entered a wrong input")
        else:
            print("You have entered a wrong option")
else:
    print("Thanks for visiting")


    