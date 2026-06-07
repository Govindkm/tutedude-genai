# Functions Quick Revision

## What It Is
Functions are reusable blocks of code that take inputs, do work, and return outputs.

## Syntax at a Glance
```python
def final_price(price, discount=0):
    return price * (100 - discount) / 100

def min_max(numbers):
    return min(numbers), max(numbers)

def best_score(*scores):
    return max(scores)

print(final_price(1000, 10))
small, big = min_max([5, 1, 9, 3])
print(small, big)
print(best_score(65, 88, 72, 91))
```

## 3 Key Things to Remember
- Use `return` to send results back.
- Default parameters work when caller skips that argument.
- `*args` collects multiple positional inputs into a tuple.

## One Gotcha
If you forget `return`, Python returns `None`, which can break later logic.

## Use This When...
Use functions when logic repeats, or when you want clean, testable code blocks.
