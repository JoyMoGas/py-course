def weather_condition(temperature):
  if temperature > 7:
    return "Warm"
  else:
    return "Cold"
  
user_input = input("Enter temperature:")
print(weather_condition(user_input))