# Object-Oriented Programming Basics

## What It Is
Object-oriented programming (OOP) is a way to structure code by bundling data and behavior into reusable class blueprints and object instances.

## Syntax At A Glance
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        return "Pass" if self.marks >= 40 else "Fail"

student1 = Student("Govind", 87)
print(student1.result())
```

## 3 Key Things to Remember
1. A class is a blueprint; an object is an instance created from that blueprint.
2. `__init__` runs automatically during object creation and initializes instance data.
3. Instance methods must include `self` as the first parameter.

## Gotcha to Avoid
Forgetting `self` in method definitions causes argument errors when calling methods from objects.

## Use This When...
Use OOP when related data and actions should stay together, such as students with marks and result logic.
