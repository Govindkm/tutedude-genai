# Python Inheritance

## What it is

Inheritance lets a child class reuse and extend attributes and methods from a parent class.

## Syntax at a glance

```python
class Child(Parent):
    def __init__(self, value):
        super().__init__(value)

    def method(self):
        return "Child behavior"
```

## Remember

1. A child class inherits accessible parent behavior.
2. Use `super()` to reuse parent initialization or methods.
3. Method overriding lets a child customize inherited behavior.
4. Polymorphism lets different child objects respond to the same method name in their own way.
5. Python uses `__mro__` to show method lookup order in multiple inheritance.

## Gotcha

Use inheritance for a clear **is-a** relationship. Use composition when one object contains or uses another object instead.

## Use this when...

Several related classes share common behavior, but each specialized class needs additional or customized behavior.
