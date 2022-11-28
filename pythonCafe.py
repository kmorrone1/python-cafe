"""
Name: Katie Morrone
Directory ID: kmorrone
Date: 2022-05-13
Assignment: Final Project
"""
'''defining variables'''
menu  = {"Brewed Coffee": 2.00, "Latte": 3.00, "Mocha": 3.75, "Tea": 1.50, 
         "Donut": 1.75, "Cookie": 1.50, "Scone": 3.25}

'''Outprint the greeting message'''
print("Welcome to Python Cafe.")

def getUserStatus(userInput):
    if (userInput == '1'):
        status = "Customer"
    
    elif (userInput == '2'):
        status = "Employee"
    
    else:
        status = "none"
    
    return status

'''main code'''
endLoop = 0
while endLoop == 0:
    status = input("Are you a customer or an employee? Please enter 1 for"
                   " customer or 2 for employee. ")
    
    if status == '1':
        print("You are a " + getUserStatus(status) + ".")
        endLoop = 1
        order = []
        print("Menu:",', '.join(list(menu.keys())))
        prompt = "What items would you like? Type done when order is complete. "
        
        while True:
           item = input(prompt)
           listLen = len(list(menu.keys()))
           
           if item in menu:
              order.append(item)
              listLen = listLen + 1
           
           elif item == "done" or item == "DONE" or item == "Done":
              break
          
           else:
               print("That item does not appear to be on the menu. Sorry.")
               print("Menu:",', '.join(list(menu.keys())))
           prompt = "Enter an additional item, type done if order is complete: "
        print("\n Your order is: %s" % (', '.join(order)))

        if listLen > 7:
            print("Thank you for ordering:",order)
        
        correctOrder = input("Does this order look correct? ")
        if correctOrder == "No":
            
            addOrRemove = input("Sorry to hear that. Would you like to remove"
                                " or add an item? ")
            
            if addOrRemove == "Remove":
                item = input("Which item? ")
                
                for i in range(len(order)):
                    
                    if item in order:
                        order.remove(item)
                        
            elif addOrRemove == "Add":
                item = input("Which item from the menu would"
                             " you like to add? ")
                order.append(item)
            
            print("\n Your new order is: %s" % (', '.join(order)))
            correctOrder = input("Does this order look correct? ")
                    
        if correctOrder == "Yes":
            price = 0
            for i in order:
                if i in menu:
                    price = price + menu[i]
            print("The total price is: $" + str(price))
        elif correctOrder == "No":
            print("Sorry. We can no longer serve you. ")
        else:
            print("Sorry. That was not a valid response.")

        
    elif status == '2':  
        print("You are a " + getUserStatus(status) + ".")
        endLoop = 1
        task = input("What would you like to do today? Access"
                     " Schedule or View Payroll. ")
        
        if task == "Access Schedule":
            f = open("/Users/katiemorrone/Documents/pythonCafeSchedule.txt", "r")
            schedule = f.readlines()
            date = input("What day of the week would you like to view? ")
            for shift in schedule:
                if date in shift:
                    print("You have work on " + shift)
        
        elif task == "View Payroll":
            f = open("/Users/katiemorrone/Documents/pythonCafePayroll.txt", "r", errors='ignore')
            payroll = f.readlines()
            print("PARTNER IDs: 1   2   3   4   5   6")
            ID = input("What is your Partner ID? ")
            if int(ID) in range(7):

                for payment in payroll:
                    if str(ID) in payment[1]:
                        payment = payment.split()
                        partnerID = payment[0]
                        hours = payment[1]
                        earnings = payment[2]
                        print("Partner ID:",partnerID,"\nHours:",hours,
                              "\nEarnings: $" + earnings)
            
            else:
                print("That is not a valid ID. Please refresh the page and"
                      " try again. ")
        
        
    
        else:
            print("That is not a valid option. Please try again.")
            endLoop = 0
        
