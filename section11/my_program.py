"""
* Class 87 - 88
myFile = open("fruits.txt")
# print(myFile.read())
content = myFile.read()

print(content)
print(content)


* Class 89
myfile = open('fruits.txt')
content = myfile.read()
myfile.close()

print(content)

* Class 91
with open('fruits.txt') as myfile:
  content = myfile.read()


print(content)

with open('files/fruits.txt') as myfile:
  content = myfile.read()

print(content)

* Class 92
with open('files/fruits.txt', 'w') as myfile:
  myfile.write("tomato\nCucumber\nOnion\n")
  myfile.write("Garlic")

* Class 93


"""

with open('files/fruits.txt', 'a+') as myfile:
  myfile.write('\nOkra')
  myfile.seek(0)
  content = myfile.read()

print(content)