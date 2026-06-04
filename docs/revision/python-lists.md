# 📝 Revision Card — Python Lists

**What it is:** An ordered, mutable collection of items accessible by index.

---

## ⚡ Syntax at a Glance

```python
# Create
my_list = [1, 2, 3]

# Access
my_list[0]       # first → 1
my_list[-1]      # last  → 3

# Modify
my_list.append(4)          # add to end
my_list.insert(1, 99)      # insert at index
my_list.remove(99)         # remove by value
my_list.pop(0)             # remove by index

# Useful functions
len(my_list)               # length
sum(my_list)               # total
sorted(my_list)            # new sorted list (non-destructive)
my_list.sort()             # sort in-place

# Find index (with start offset)
my_list.index(val, start)  # find second occurrence

# Zip two lists
for a, b in zip(list1, list2): ...

# Enumerate (index + value)
for i, val in enumerate(my_list, start=1): ...

# List comprehension
result = [expr for x in my_list if condition]
result = [x for x, y in zip(l1, l2) if y > 75]
```

---

## 3 Key Things to Remember

1. **`sorted()` vs `.sort()`** — `sorted()` returns a new list; `.sort()` modifies in-place and returns `None`
2. **`enumerate(list, start=1)`** — gives `(index, value)` pairs; `start` lets you begin at any number
3. **List comprehension** — `[expr for item in list if cond]` replaces most manual `for`+`append` loops

---

## ⚠️ One Gotcha to Avoid

```python
# ❌ Wrong — .sort() returns None, not the sorted list
result = my_list.sort()   # result is None!

# ✅ Correct
my_list.sort()
result = my_list          # or use sorted()
result = sorted(my_list)
```

---

## 🧭 Use This When...

> *"I need to store an ordered collection of items and iterate, filter, or transform them."*
