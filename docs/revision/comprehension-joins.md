# 📝 Comprehension Joins — Quick Revision

## What is it?
A comprehension join combines rows from two or more collections by matching related keys (like IDs) in a single expression.

## Syntax At A Glance
```python
# 2-table join (list of tuples)
joined = [
    (s["name"], e["course_id"])
    for s in students
    for e in enrollments
    if s["student_id"] == e["student_id"]
]

# 3-table join (student + enrollment + course)
student_course = [
    (s["name"], c["course"])
    for s in students
    for e in enrollments
    for c in courses
    if s["student_id"] == e["student_id"] and e["course_id"] == c["course_id"]
]
```

## 3 Key Things To Remember
- Match using stable keys (`student_id`, `course_id`, `order_id`) not names.
- Build helper maps when join chains become long.
- Keep conditions explicit; wrong join conditions create duplicate/wrong rows.

## Gotcha To Avoid
Forgetting one join condition creates a Cartesian product (too many rows).

## Use This When...
Use comprehension joins when you need SQL-like joins and quick derived lists/dicts without writing full loops.
