# Python Loops Quick Revision

## What It Is
Loops repeat a block of code so you do not write the same logic again and again.

## Syntax at a Glance
```python
# for loop
for i in range(1, 4):
    print(i)

# while loop
n = 3
while n > 0:
    print(n)
    n -= 1

# nested loop
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
```

## 3 Key Things to Remember
- `for` is great for sequences/ranges.
- `while` needs careful condition updates.
- Nested loops multiply total iterations.

## One Gotcha
Forgetting to update a `while` loop variable can create an infinite loop.

## Use This When...
Use loops when you need to process repeated items, build tables/grids, or generate combinations.
