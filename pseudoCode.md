# Part 1 pseudo code

```
print intro message
get categoryInput
while categoryInput != 0
    if categoryInput is not in (0, 1, 2, 3, 4, 5)
        print error message 
        continue
    
    if categoryInput is 0
        break
    
    elif categoryInput is 1
        get quantityInput
        do profit calculation
    
    ...

    elif categoryInput is 5
        get quantityInput
        do profit calculation

add profit from all categories
print total profit
```

# Part 2 pseudo code

Code in part 1 will be represented as 
```
dailyProfit()
```

Checking if inputs (are suppose be numbers) are numbers **is not included** in pseudo code

```
print intro message
get timePeriodSelection
while timePeriodSelection != 0
    if timePeriodSelection is not in (0, 1, 2, 3, 4)
        print error message 
        continue
    
    #theto part start
    if timePeriodSelection is 0
        break
    
    elif timePeriodSelection is 1
        get dayInput
        accept both uppercase and lowercase and mixed
        dailyProfit()
        print total profit for the day
        
    elif timePeriodSelection is 2
        for day in week
            dailyProfit()
            add to total profit of previous days
        print total profit

        #theto part end


    #ethan part start
    elif timePeriodSelection is 3
        for day in weekdays
            dailyProfit()
            add to total profit of previous days
        print total profit

    elif timePeriodSelection is 4
        for day in weekend
            dailyProfit()
            add to total profit of previous days
        print total profit

    if totalProfit >= $10,000
        print “You did well this period! Keep up the great work!”
    elif totalProfit < $10,000
        print “We didn’t reach our goal for this period. More work is needed.”

print program end
```

#ethan part end     