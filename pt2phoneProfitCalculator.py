
def dailyProfit():
    #creating a dictionary for product categories & profit margins
    productCategory = {1:120.45, #apple iphone
                    2:99.50, #android phone
                    3:75.69, #apple tablet
                    4:65.73, #android tablet
                    5:51.49} #windows tablet
    totalProfit = 0

    #get product category input
    categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

    while categoryInput != 0: 
    #error message for invalid input
        if categoryInput not in (0,1,2,3,4,5):
            print("Invalid input, please enter a valid number.")
        else:
            if categoryInput ==  1:
                quantityInput = int(input("Enter quantity sold: \n"))
                profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                totalProfit += profit #add the profit to the total amount of profit
            elif categoryInput == 2:
                quantityInput = int(input("Enter quantity sold: \n"))
                profit = productCategory[2] * quantityInput
                totalProfit += profit
            elif categoryInput == 3:
                quantityInput = int(input("Enter quantity sold: \n"))
                profit = productCategory[3] * quantityInput
                totalProfit += profit
            elif categoryInput == 4:
                quantityInput = int(input("Enter quantity sold: \n"))
                profit = productCategory[4] * quantityInput
                totalProfit += profit
            elif categoryInput == 5:
                quantityInput = int(input("Enter quantity sold: \n"))
                profit = productCategory[5] * quantityInput
                totalProfit += profit
        #continue to ask for product category
        categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))
    return totalProfit
  

#print intro message
print("Welcome to Circle Phones’ Profit calculator.\n")


while True:
    timePeriodSelection = int(input("""You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend

    Enter:
    1 - For specific Day
    2 - For the Week
    3 - For Week Business Days
    4 - For Weekend days
    0 - Exit \n"""))
    if timePeriodSelection not in (0, 1, 2, 3, 4):
        print('Invalid input, please enter a valid input')
        continue
    if timePeriodSelection == 0:
        break

    if timePeriodSelection == 1:

# Theto started here if user choose 1 

        # if the user choose number 1

        # input and testing an inputed day if Monday to Sunday
        x = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]')
        day = x.capitalize()
        print(f'For {day}')

        # The following is from part 1

        totalProfit = 0

        #creating a dictionary for product categories & profit margins
        productCategory = {1:120.45, #apple iphone
                           2:99.50, #android phone
                           3:75.69, #apple tablet
                            4:65.73, #android tablet
                            5:51.49} #windows tablet

        #get product category input
        categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

        while categoryInput != 0:
        #error message for invalid input
            if categoryInput not in (0,1,2,3,4,5):
                print("Invalid input, please enter a valid number.")
            else:              
                if categoryInput ==  1:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                    totalProfit += profit #add the profit to the total amount of profit
                elif categoryInput == 2:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[2] * quantityInput
                    totalProfit += profit
                elif categoryInput == 3:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[3] * quantityInput
                    totalProfit += profit
                elif categoryInput == 4:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[4] * quantityInput
                    totalProfit += profit
                elif categoryInput == 5:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[5] * quantityInput
                    totalProfit += profit
        #continue to ask for product category
        categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

        #print total
        print(f"Your total profit for {day} is: ${totalProfit:.2f}") # Theto Edited this part to match the output of part 2
        print("More hard work needed... The last Monday wasn't the best") #this is new

# Theto ended here if user choose 1          

    elif timePeriodSelection == 2:
        
# Theto started here if user choose 2 
    
        # if the user choose number 2
        count = 0
        totalProfit = 0
        while count != 7:   # count 7 times for Monday - Sunday
            count = count+1
   
            # input and testing an inputed day if Monday to Sunday
            x = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]')
            day = x.capitalize()
            print(f'For {day}')

            # The following is from part 1


            #creating a dictionary for product categories & profit margins
            productCategory = {1:120.45, #apple iphone
                               2:99.50, #android phone
                               3:75.69, #apple tablet
                               4:65.73, #android tablet
                               5:51.49} #windows tablet

            #get product category input
            categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

            while categoryInput != 0:
            #error message for invalid input
                if categoryInput not in (0,1,2,3,4,5):
                    print("Invalid input, please enter a valid number.")
                else:
                    if categoryInput ==  1:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                        totalProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[2] * quantityInput
                        totalProfit += profit
                    elif categoryInput == 3:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[3] * quantityInput
                        totalProfit += profit
                    elif categoryInput == 4:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[4] * quantityInput
                        totalProfit += profit
                    elif categoryInput == 5:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[5] * quantityInput
                        totalProfit += profit
                #continue to ask for product category
                categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

        #print total
        print(f"Your total profit for {day} is: ${totalProfit:.2f}") # Edited this part to match the output of part 2
        print("You did good this week") #this is new

# Theto ended here if user choose 2 

    elif timePeriodSelection == 3:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in weekdays:
            weekdaysProfit = 0
            print("For",day)
            dailyProfit() #replace with function content/remove function
            weekdaysProfit += dailyProfit
        print(f"Total Profit for the week (business days) is: ${weekdaysProfit}")



    elif timePeriodSelection == 4:
        continue


print('Program End!')
