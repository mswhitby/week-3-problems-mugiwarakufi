def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x,y):
  return x / y
def exponent(x, y):
  return x ** y

print("ON")

while True:
  choice = input("CHOOSE AN OPERATION: (1/2/3/4/5):\n1. Addition\n2. Subraction\n3. Multiplication\n4. Division\n5. Exponentiation\n")
  
  if choice in ('1', '2', '3', '4', '5'):
      first_number = float(input("Enter first number: "))
      second_number = float(input("Enter second number: "))
      
      if choice == '4':
        if second_number != 0:
          print("result: ",divide(first_number, second_number))
        else:
          print("Can't divide by 0!")
      
      if choice == '1':
        print('result: ',add(first_number, second_number))
        
      elif choice == '2':
        print('result: ',subtract(first_number, second_number))

      elif choice == '3':
        print('result: ',multiply(first_number, second_number))
      
      elif choice == '5':
        print('result: ',exponent(first_number, second_number))
        
      next_calculation = input("Perform another calculation (yes/no)?")
      if next_calculation == "no":
          break
    
  else:
        print("Invalid Input")
