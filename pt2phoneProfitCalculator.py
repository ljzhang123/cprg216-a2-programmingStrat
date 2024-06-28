#creating a dictionary for product categories & profit margins
productCategory = {1:120.45, #apple iphone
                2:99.50, #android phone
                3:75.69, #apple tablet
                4:65.73, #android tablet
                5:51.49} #windows tablet

# def dailyProfit():
#     dailyProfit = 0

#     #get product category input
#     categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

#     while categoryInput != 0: 
#     #error message for invalid input
#         if categoryInput not in (0,1,2,3,4,5):
#             print("Invalid input, please enter a valid number.")
#         else:
#             if categoryInput ==  1:
#                 quantityInput = int(input("Enter quantity sold: \n"))
#                 profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
#                 dailyProfit += profit #add the profit to the total amount of profit
#             elif categoryInput == 2:
#                 quantityInput = int(input("Enter quantity sold: \n"))
#                 profit = productCategory[2] * quantityInput
#                 dailyProfit += profit
#             elif categoryInput == 3:
#                 quantityInput = int(input("Enter quantity sold: \n"))
#                 profit = productCategory[3] * quantityInput
#                 dailyProfit += profit
#             elif categoryInput == 4:
#                 quantityInput = int(input("Enter quantity sold: \n"))
#                 profit = productCategory[4] * quantityInput
#                 dailyProfit += profit
#             elif categoryInput == 5:
#                 quantityInput = int(input("Enter quantity sold: \n"))
#                 profit = productCategory[5] * quantityInput
#                 dailyProfit += profit
#         #continue to ask for product category
#         categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))
#     return dailyProfit
  
#print intro message
print("Welcome to Circle Phones’ Profit calculator.\n")


while True:
    timePeriodSelection = input("""You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend

    Enter:
    1 - For specific Day
    2 - For the Week
    3 - For Week Business Days
    4 - For Weekend days
    0 - Exit \n""")

    if timePeriodSelection.isdigit():
        timePeriodSelection = int(timePeriodSelection)
    else:
        continue
    
    if timePeriodSelection not in (0, 1, 2, 3, 4):
        print('Invalid input, please enter a valid input')
        continue

    if timePeriodSelection == 0:
        break

    if timePeriodSelection == 1:
        days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

        # input and testing an inputed day if Monday to Sunday
        day = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]').capitalize()    
        while day not in days:
            print("That's not a valid day")
            day = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]').capitalize()
        print(f'For {day}')

        dailyProfit = 0
        categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

        while categoryInput != 0:
        #error message for invalid input
            if categoryInput not in (0,1,2,3,4,5):
                print("Invalid input, please enter a valid number.")
            else:              
                if categoryInput ==  1:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                    dailyProfit += profit #add the profit to the total amount of profit
                elif categoryInput == 2:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[2] * quantityInput
                    dailyProfit += profit
                elif categoryInput == 3:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[3] * quantityInput
                    dailyProfit += profit
                elif categoryInput == 4:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[4] * quantityInput
                    dailyProfit += profit
                elif categoryInput == 5:
                    quantityInput = int(input("Enter quantity sold: \n"))
                    profit = productCategory[5] * quantityInput
                    dailyProfit += profit
        #continue to ask for product category
            categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

        #print total
        print(f"Your total profit for {day} is: ${dailyProfit:.2f}") # Theto Edited this part to match the output of part 2
        if dailyProfit >= 10000:
            print(f'You did well this past {day}! Keep up the great work!')
        else:
            print(f'We didn’t reach our goal for this past {day}. More work is needed.')    

    elif timePeriodSelection == 2:
        # if the user choose number 2
        weeklyProfit = 0
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in week:   # count 7 times for Monday - Sunday
            print(f'For {day}')

            categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

            while categoryInput != 0:
                dailyProfit = 0
            #error message for invalid input
                if categoryInput not in (0,1,2,3,4,5):
                    print("Invalid input, please enter a valid number.")
                else:
                    if categoryInput ==  1:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                        dailyProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[2] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 3:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[3] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 4:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[4] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 5:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[5] * quantityInput
                        dailyProfit += profit
                weeklyProfit += dailyProfit
                #continue to ask for product category
                categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

        #print total
        print(f"Your total profit for {day} is: ${dailyProfit:.2f}") # Edited this part to match the output of part 2
        if weeklyProfit >= 10000:
            print('You did well this week! Keep up the great work!')
        else:
            print('We didn’t reach our goal for this week. More work is needed.')

    elif timePeriodSelection == 3:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        weekdaysProfit = 0
        for day in weekdays:
            print(f"For {day}")

            dailyProfit = 0

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
                        dailyProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[2] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 3:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[3] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 4:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[4] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 5:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[5] * quantityInput
                        dailyProfit += profit

                categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))

            weekdaysProfit += dailyProfit

        print(f"Total Profit for the week (business days) is: ${weekendsProfit}")
        if weekendsProfit >= 10000:
            print('You did well this week (business days)! Keep up the great work!')
        else:
            print('We didn’t reach our goal for this week (business days). More work is needed.')


    elif timePeriodSelection == 4:
        weekends = ["Saturday", "Sunday"]
        weekendsProfit = 0
        for day in weekends:
            print(f"For {day}")
            
            dailyProfit = 0

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
                        dailyProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[2] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 3:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[3] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 4:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[4] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 5:
                        quantityInput = int(input("Enter quantity sold: \n"))
                        profit = productCategory[5] * quantityInput
                        dailyProfit += profit   
                categoryInput = int(input("Enter product number 1-5, or enter 0 to stop: \n"))        

            weekendsProfit += dailyProfit
        print(f"Total Profit for the weekend is: ${weekendsProfit}")

        if weekendsProfit >= 10000:
            print('You did well this weekend! Keep up the great work!')
        else:
            print('We didn’t reach our goal for this weekend. More work is needed.')

print('Program End!')
