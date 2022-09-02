actor = int(input("What factor would you like a list of multiples of? This must must be an integer: "))
length = int(input("Enter how long you would like your list of factors to be. This number must be an integer greater than 0: "))
def list_of_multiples(factor, length):
    return range(factor, length*factor+1, factor)
  
print list_of_multiples(factor, length)
