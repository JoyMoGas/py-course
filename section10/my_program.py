"""
* Class 79
def area(a, b):
  return a * b

print(area(2, 5))


* Class 81
def area(a, b=6):
  return a * b

print(area(a=5))


* Class 82
def mean(*args):
  return sum(args / len(args))
  #return type(args)

print(mean(1, 3, 4))

* Class 83

"""

def mean(**kwargs):
  return kwargs
  #return type(args)

print(mean(a=1, b=3, c=4))