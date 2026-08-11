# 📝 Revision Card: Python Tuples

## What is a tuple?
A tuple is an ordered, immutable collection in Python.

## Syntax at a glance
```python
colors = ("red", "green", "blue")
print(colors[0])

name, age = ("Asha", 21)

single = (5,)  # trailing comma is required for one item
```

## 3 things to remember
1. Tuples are immutable, so items cannot be changed in place.
2. Use indexing/slicing just like lists (`t[0]`, `t[1:3]`).
3. To add an item, create a new tuple: `t = t + (new_item,)`.

## One gotcha to avoid
`(5)` is just an integer in parentheses, not a tuple.
Use `(5,)` for a one-item tuple.

## Use this when...
Use tuples when values should stay fixed, such as coordinates, constant settings, or grouped return values.
