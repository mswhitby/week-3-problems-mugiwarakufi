def add(n1, n2):
  return float(n1) + float(n2)
  
n1 = input("Enter a number: ")
n2 = input("Enter a number: ")

if len(str(n1)) == 0 or len(str(n2)) == 0:
  print("Invalid Operation")
   
if len(str(n1)) != 0 or len(str(n1)) != 0:
  print(add(n1, n2))
