"""
* Class 40 - 44

"""

def mean(value):
  the_mean = sum(value) / len(value)
  return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades))