"""
* Class 54

def weather_condition(temperature):
  if temperature > 7:
    return "Warm"
  else:
    return "Cold"
  
user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))
"""

user_input = input('Enter yout name:')
message1 = 'Hello %s' %user_input
message = f"Hello {user_input}"
print(message)