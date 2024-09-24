'''
Jagger Vasquez - To Do list
make a to-do list and print it out

use remove and imput commands to have the user type in and remove items from list
Made it loop thanks to while
'''
toDoList=["wake up", "get food", "go study", "work", "shower", "sleep"]

for i in range (len(toDoList)):
    print(toDoList[i])
    
while toDoList[i>0]:
    toDoList.remove(input("\nWhat do you want to do? "))
    for i in range (len(toDoList)):
        print(toDoList[i])
if toDoList[i==0]:
    print("all tasks are finished")