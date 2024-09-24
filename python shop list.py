'''
Jagger Vasquez - Shop list

Make a nested list of items in a shop.
Use for loop to make the list
Second for loop to try and identify each item
'''
shopList=[("Egg",0.99),
          ("Bread",1.99),
          ("Fruits", 2.99)]

for entry in shopList:
    item, price = entry
    print(item, ":", price)
    
uPick=input("What will you like to buy? ")

for entry in shopList:
    item, price = entry
    if uPick == item:
        print("Here's your", item, "That will be", price)
        break
    else:
        print ("I don't have that. Get lost!")