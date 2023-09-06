toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):
    toDoList.remove(item)

userAns = input("Do you want to add to your list, remove from your list or quit? A/R/Q")
while userAns == "A" or userAns == "R":
    if userAns == "A":
        item = input("What item do you want to add?")
        addItem(item)
    else:
        item = input("What item do you want to remove?")
        deleteItem(item)
        
    userAns = input("Do you want to add to your list, remove from your list or quit? A/R/Q")