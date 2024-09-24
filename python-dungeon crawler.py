'''
Jagger Vasquez - Dungeon Crawler

Fuck tons of if/while loops. Who am I? Yandere Dev?
Random for monster encounters, healing, damage, and/or money
List of commands shown
'''
import random #rngsus bless us with your gift of light

score = 200
health = 20
maxHealth = 20
uName = input("Enter your name: ")
defCommands = ("Search",
               "Rest",
               "Shop",
               "Score",
               "Inventory",
               "End")

inventory = ["Sword",
             "Handguns"]
               
print("Your commands are", defCommands)

uCommand = input("\nwhat will you do? ")

#game loop time (oh boy)
while uCommand != "End": #forgot to do this, derp

    if uCommand == "Rest": #recovers HP
        if health < maxHealth: #RNG based recovery
            recoverHP = random.randint(1,5)
            health += recoverHP
            print("recovered", recoverHP, "health")
            uCommand = input("\nNow what? ")
        if health == maxHealth: #Making sure it doesn't overflow
            print("alredy fully rested")
            uCommand = input("\nNow what? ")
            
    if uCommand == "Score": #displays user score
        print(uName, "you have", score, "points")
        uCommand = input("\nNow what? ")
        
    if uCommand == "Inventory": #displays inventory
        if not inventory:
            print("You are empty-handed")
        else:
            print(inventory)
        uCommand = input("\nNow what? ")
    
    if uCommand == "Shop":
        
        shoplist=[("Amulet", 500), ("Shotgun", 300)]
        
        for entry in shoplist:
            item, price = entry
            print(item, ":", price)
            
        uPick=input("What're you buyin', stranger? (type 'Exit' to leave) ") #RE4 Merchant sells you things
        if uPick == item and score >= price:
            score -= price
            shopList.remove(entry)
            inventory.append(item)
            print("Heh, heh, heh, thank you!")
            uPick=input("What're you buyin', stranger? (type 'Exit' to leave) ")
        if uPick != item or score < price: #When you're broke
            print("Sorry, stranger")
            uPick=input("What're you buyin', stranger? (type 'Exit' to leave) ")
        if uPick == "Exit": #Leaves shop
            print("Come again, Stranger!")
            uCommand = input("\nNow what? ")
    
    if uCommand == "Search": #Fight loop FUUUUUUUUUUUCK
        searchNum = random.randint(1,2)
        
        if searchNum == 1:
            print("There are no demons here")
            uCommand = input("\nNow what? ")
            
        if searchNum == 2:
            
            demonHP = 10
            demonMaxHP = 10
            uFightAction=("Fight", "Run")
            print(uFightAction)
            uFightAct = input("You encounter a monster: what do? ")
            
            while uFightAct=="Fight": #Keep fighting, making sure it doesn't break out of loop
                damageCombat = random.randint(1,5)
                print("Deal", damageCombat, "to monster") 
                demonHP -= damageCombat
                damageCombat = random.randint(1,5)
                print("monster deals", damageCombat, "to you")
                health -= damageCombat
                uFightAct = input("Now what? ")
            
                if demonHP == 0: #You Win!
                    reward = random.randint(100,300)
                    print("You got", reward)
                    score += reward
                    break
                    uCommand = input("\nNow what? ")
                
                if uFightAct == "Run": #Coward
                    print("You ran away")
                    break
                    uCommand = input("\nNow what? ")

if health == 0: #You are dead! Dead! Dead!
    print("You died\n", uName, "final score is:", score)
    
if uCommand == "End": #User ended command
    print(uName, "final score is:", score) #Fucking 114 lines of code