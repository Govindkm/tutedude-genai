from math_utils import add, subtract, square
import string_utils
import shop_package.discount as disc
from shop_package.billing import apply_tax, calculate_total

# Example tests to run from main.py:
print(add(10, 5))
print(subtract(10, 5))
print(square(7))

# Example tests:
print(string_utils.capitalize_words("hello python world"))
print(string_utils.reverse_string("module"))

# Suggested output checks:
print(calculate_total([400, 600, 250, 100]))
print(disc.apply_discount(1000, 20))
print(disc.bulk_discount(500))
print(apply_tax(300))