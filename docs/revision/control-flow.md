# Control Flow Quick Revision

## What It Is
Control flow lets your program choose different paths using conditions.

## Syntax at a Glance
```python
score = 75

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Good job")
else:
    print("Keep practicing")
```

## 3 Key Things to Remember
- Order matters: check stricter conditions first.
- Use `==` for equality checks (not `=`).
- Indentation defines the block in Python.

## One Gotcha
If you place a broad condition first (like `score >= 60`), later stricter checks (like `score >= 90`) may never run.

## Use This When...
Use control flow when your output/action should change based on values or user choices.
