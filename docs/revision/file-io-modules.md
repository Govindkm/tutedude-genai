# File I/O and Modules Quick Revision

## What It Is
File I/O lets Python programs save and load data using files, while modules let you reuse built-in or external code by importing it.

## Syntax at a Glance
```python
# File I/O
with open("study_log.txt", "a") as f:
    f.write("Read docs|study|25|done\n")

with open("study_log.txt", "r") as f:
    lines = f.readlines()

# Module imports
import math
from random import randint
import datetime as dt

print(math.sqrt(49))
print(randint(1, 10))
print(dt.date.today())
```

## 3 Key Things to Remember
- Use `with open(...)` so files close automatically.
- Choose file mode carefully: `w` overwrite, `a` append, `r` read.
- Convert numeric text from files (like minutes) to `int` before calculations.

## One Gotcha
If you append without `\n`, the next record can stick to the previous line and break parsing.

## Use This When...
Use File I/O when you need persistent data, and use modules when you want ready-made functionality instead of rewriting common utilities.
