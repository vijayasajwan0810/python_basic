#!/usr/bin/python

class Employee:
  'Common base class'
  empCount = 0

  def __init__(self, name, sal):
    self.name = name
    self.sal = sal
    Employee.empCount += 1

  def displayCount(self):
   print "Total Emp %d " % Employee.empCount
  def displayEmp (self):
   print "Name:",self.name, ",Salarry: ",self.sal

#emp1=Employee("Zara", 2000)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmp ()
emp2.displayEmp ()

print "Total Emp %d" %Employee.empCount


