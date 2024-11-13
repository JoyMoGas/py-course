"""
* Class 59

"""

monday_temperatures = [9.1, 8.8, 7.9]

print(round(monday_temperatures[0]))
print(round(monday_temperatures[1]))
print(round(monday_temperatures[2]))

for temperature in monday_temperatures:
  print(round(temperature))

print('-------------------')

for letter in 'hello':
  print(letter)



def celsius_to_kelvin(cels):
    return cels + 273.15

for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))