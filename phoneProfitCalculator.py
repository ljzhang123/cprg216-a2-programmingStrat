#print intro message
print("Welcome to Circle Phones’ Profit calculator.")

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
print(f"Your total profit for today is: {totalProfit}")