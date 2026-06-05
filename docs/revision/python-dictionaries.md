# 📝 Python Dictionaries — Quick Revision

## What is it?
A dictionary stores data as key-value pairs, like a contact book where a name points to a phone number.

## Syntax At A Glance
```python
student = {"name": "Asha", "marks": 91}

# read
print(student["name"])
print(student.get("grade", "NA"))

# write
student["marks"] = 95
student["grade"] = "A"

# loop
for name, value in student.items():
    print(name, value)

# comprehension
passed = {n: s for n, s in gradebook.items() if s >= 75}
```

## 3 Key Things To Remember
- Keys must be unique and immutable (`str`, `int`, `tuple` etc.).
- Use `get()` for safe lookup when keys may be missing.
- Use `.items()` when you need both key and value in loops/comprehensions.

## Gotcha To Avoid
Direct access of missing keys throws `KeyError`:
```python
d = {"a": 1}
# d["b"]  # KeyError
d.get("b", 0)  # safe
```

## Use This When...
Use dictionaries when you need fast lookup by label (name, id, code) instead of numeric index positions.
