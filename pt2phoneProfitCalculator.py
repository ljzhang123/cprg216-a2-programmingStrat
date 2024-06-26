#creating a dictionary for product categories & profit margins
productCategory = {1:120.45, #apple iphone
                2:99.50, #android phone
                3:75.69, #apple tablet
                4:65.73, #android tablet
                5:51.49} #windows tablet
  
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

    # Check if user input is a digit before casting into int
    if timePeriodSelection.isdigit():
        timePeriodSelection = int(timePeriodSelection)
    else:
        print('Please enter a valid digit')
        continue
    
    if timePeriodSelection not in (0, 1, 2, 3, 4):
        print('Invalid input, please enter a valid input')
        continue

    if timePeriodSelection == 0:
        break

    if timePeriodSelection == 1:
        days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

        # input and testing an inputed day if Monday to Sunday, convert all with capitalize() to accept all lowercase and uppercase scenarios
        day = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n').capitalize()   
        while day not in days:
            print("That's not a valid day")
            day = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n').capitalize()
        print(f'For {day}')

        dailyProfit = 0

        # part1 logic, calculates the daily profit
        # TODO: snippet start
        while True:
            categoryInput = input("Enter product number 1-5, or enter 0 to stop: \n")

            if categoryInput.isdigit():
                categoryInput = int(categoryInput)
            else:
                print('Please enter a valid digit')
                continue

            if categoryInput not in (0,1,2,3,4,5):
                print("Invalid input, please enter a valid number.")

            elif categoryInput == 0:
                break

            else:    
                quantityInput = input("Enter quantity sold: \n")
                while quantityInput.isdigit() == False:
                    print('Please enter a valid digit')
                    quantityInput = input("Enter quantity sold: \n")

                quantityInput = int(quantityInput)

                if categoryInput ==  1:
                    profit = productCategory[1] * quantityInput 
                    dailyProfit += profit 
                elif categoryInput == 2:
                    profit = productCategory[2] * quantityInput
                    dailyProfit += profit
                elif categoryInput == 3:
                    profit = productCategory[3] * quantityInput
                    dailyProfit += profit
                elif categoryInput == 4:
                    profit = productCategory[4] * quantityInput
                    dailyProfit += profit
                elif categoryInput == 5:
                    profit = productCategory[5] * quantityInput
                    dailyProfit += profit
        # TODO: snippet end

        #print total
        print(f"Total profit for the {day} is: ${dailyProfit:.2f}")
        if dailyProfit >= 10000:
            print(f'You did well this past {day}! Keep up the great work!')
        else:
            print(f"More hard work needed... The last {day} wasn't the best")

    elif timePeriodSelection == 2:
        weeklyProfit = 0
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in week:
            print(f'For {day}')

            dailyProfit = 0

            # part1 logic, calculates the daily profit
            while True:
                categoryInput = input("Enter product number 1-5, or enter 0 to stop: \n")
                
                if categoryInput.isdigit():
                    categoryInput = int(categoryInput)
                else:
                    print('Please enter a valid digit')
                    continue

                if categoryInput not in (0,1,2,3,4,5):
                    print("Invalid input, please enter a valid number.")

                elif categoryInput == 0:
                    break

                else:
                    quantityInput = input("Enter quantity sold: \n")
                    while quantityInput.isdigit() == False:
                        print('Please enter a valid digit')
                        quantityInput = input("Enter quantity sold: \n")

                    quantityInput = int(quantityInput)

                    if categoryInput ==  1:
                        profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                        dailyProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        profit = productCategory[2] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 3:
                        profit = productCategory[3] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 4:
                        profit = productCategory[4] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 5:
                        profit = productCategory[5] * quantityInput
                        dailyProfit += profit

            weeklyProfit += dailyProfit
            
        # print total
        print(f"Total profit for the week is: ${weeklyProfit:.2f}") 
        if weeklyProfit >= 10000:
            print('You did good this week')
        else:
            print('We didn’t reach our goal for this week. More work is needed.')

    elif timePeriodSelection == 3:
        weekdaysProfit = 0
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        for day in weekdays:
            print(f"For {day}")

            dailyProfit = 0

            # part1 logic, calculates the daily profit
            while True: 
                categoryInput = input("Enter product number 1-5, or enter 0 to stop: \n")

                if categoryInput.isdigit():
                    categoryInput = int(categoryInput)
                else:
                    print('Please enter a valid digit')
                    continue

                #error message for invalid input
                if categoryInput not in (0,1,2,3,4,5):
                    print("Invalid input, please enter a valid number.")
                
                elif categoryInput == 0:
                    break

                else:
                    quantityInput = input("Enter quantity sold: \n")
                    while quantityInput.isdigit() == False:
                        print('Please enter a valid digit')
                        quantityInput = input("Enter quantity sold: \n")

                    quantityInput = int(quantityInput)

                    if categoryInput ==  1:
                        profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                        dailyProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        profit = productCategory[2] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 3:
                        profit = productCategory[3] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 4:
                        profit = productCategory[4] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 5:
                        profit = productCategory[5] * quantityInput
                        dailyProfit += profit


            weekdaysProfit += dailyProfit

        print(f"Total Profit for the week (business days) is: ${weekdaysProfit:.2f}")
        if weekdaysProfit >= 10000:
            print('You did good this week (business days)')
        else:
            print('We didn’t reach our goal for this week (business days). More work is needed.')


    elif timePeriodSelection == 4:
        weekendsProfit = 0
        weekends = ["Saturday", "Sunday"]
        
        for day in weekends:
            print(f"For {day}")
            
            dailyProfit = 0

            # part1 logic, calculates the daily profit
            while True: 
                categoryInput = input("Enter product number 1-5, or enter 0 to stop: \n")
                
                if categoryInput.isdigit():
                    categoryInput = int(categoryInput)
                else:
                    print('Please enter a valid digit')
                    continue

                #error message for invalid input
                if categoryInput not in (0,1,2,3,4,5):
                    print("Invalid input, please enter a valid number.")

                elif categoryInput == 0:
                    break
                
                else:
                    quantityInput = input("Enter quantity sold: \n")
                    while quantityInput.isdigit() == False:
                        print('Please enter a valid digit')
                        quantityInput = input("Enter quantity sold: \n")

                    quantityInput = int(quantityInput)

                    if categoryInput ==  1:
                        profit = productCategory[1] * quantityInput #access the value in the dictionary by using the key
                        dailyProfit += profit #add the profit to the total amount of profit
                    elif categoryInput == 2:
                        profit = productCategory[2] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 3:
                        profit = productCategory[3] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 4:
                        profit = productCategory[4] * quantityInput
                        dailyProfit += profit
                    elif categoryInput == 5:
                        profit = productCategory[5] * quantityInput
                        dailyProfit += profit   

            weekendsProfit += dailyProfit
            
        print(f"Total Profit for the weekend is: ${weekendsProfit:.2f}")

        if weekendsProfit >= 10000:
            print('You did good this weekend')
        else:
            print('We didn’t reach our goal for this weekend. More work is needed.')

print('Program End!')
