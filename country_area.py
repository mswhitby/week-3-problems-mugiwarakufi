country = input("country name: ")
area = float(input("enter area of country (in square kilometers - refrain from using commas in your input): "))

def area_of_country(country, area):
  landmass = 148940000
  proportion = area * 100 / landmass
  
  sentence = "{} is {:.2f} percent of the total world's landmass".format(country,proportion)
  print(sentence)
  
area_of_country(country, area)
