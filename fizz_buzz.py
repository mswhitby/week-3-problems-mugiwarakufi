buzzbuzzbuzz = int(input("Enter an integer: "))

def fizz_buzz(buzzbuzzbuzz):
  if buzzbuzzbuzz % 3 == 0 and buzzbuzzbuzz % 5 == 0:
    print("FizzBuzz")
  elif buzzbuzzbuzz % 3 == 0:
    print("Fizz")
  elif buzzbuzzbuzz % 5 == 0:
    print("Buzz")
  else:
    print(buzzbuzzbuzz)
  
fizz_buzz(buzzbuzzbuzz)
