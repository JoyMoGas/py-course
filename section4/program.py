"""
* Class 33
monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
len(monday_temperatures) # 5

monday_temperatures[3]  # 6.6

monday_temperatures[1:4] # [8.8, 7.5, 6.6].

monday_temperatures[0:2] # [9.1, 8.8]

monday_temperatures[:2] # [9.1, 8.8]

monday_temperatures[3:5] # [6.6, 9.9]

monday_temperatures[3:] # [6.6, 9.9]

monday_temperatures[4] # 9.9

monday_temperatures[-1] # 9.9

monday_temperatures[-2:] # [6.6, 9.9]

monday_temperatures[-4:-2] # [8.8, 7.5]

mystring = 'hello'
mystring[1] # e
mystring[-1] # o
mystring[:3] # hel

monday_temperatures = ["hello", 1, 2, 3]
monday_temperatures[0] # hello
monday_temperatures[0][2] # l
"""


studen_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
search_engines_users = {"google": 1000000000, "bing": 127000000, "duck duck go":12000000}
eng_port = {"rain": "chuva", "sun": "sol"} 

"""
From tuple to list:

>>> cool_tuple = (1, 2, 3)
>>> cool_list = list(cool_tuple)
>>> cool_list
[1, 2, 3]


From list to tuple:

>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> cool_tuple
(1, 2, 3)


From string to list:

>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']


From list to string:

>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'
"""