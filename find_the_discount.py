price = int(input("Enter the original price of our item or combined price of your items. This number should be a whole number. "))
discount = int(input("Enter the rate of the discount. This number should be a whole number between 0 and 100. "))

def dis(price, discount):
  final_price = price * (100 - discount) / 100
  
  disfinal = "{:.2f}".format(final_price)
  print(disfinal)
  
dis(price, discount)
