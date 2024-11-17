"""
* Class 96
import time

while True:
  with open('files/vegetables.txt') as file:
    print(file.read())
    time.sleep(10)



* Class 97
import time
import os

while True:
  if os.path.exists('files/vegetables.txt'):
    with open('files/vegetables.txt') as file:
      print(file.read())
  else:
    print('File does not exist.')
  time.sleep(10)


* Class 98 - 99
"""

import time
import os
import pandas

while True:
  if os.path.exists('files/temps_today.csv'):
    data = pandas.read_csv("files/temps_today.csv")
    print(data.mean()['st1'])
  else:
    print('File does not exist.')
  time.sleep(10)

