# 1. Creating and accessing set elements
fruits = {"apple", "banana", "cherry"}

print("Accessing Elements")
print(f"Set contents: {fruits}")

# Since sets are unordered, you cannot access elements by index.
# You access them by iterating through the set:
print("Iterating through the set:")
for fruit in fruits:
    print(f"{fruit}")

# 2. Defining sets for mathematical operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_a.add(6)

print("\n--- Set Operations ---")
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: All unique elements from both sets
# Use the | operator or the .union() method
union_set = set_a | set_b
print(f"Union (A ∪ B): {union_set}")

# Intersection: Elements present in both sets
# Use the & operator or the .intersection() method
intersection_set = set_a & set_b
print(f"Intersection (A ∩ B): {intersection_set}")

# Difference: Elements in A that are NOT in B
# Use the - operator or the .difference() method
difference_set = set_a - set_b
print(f"Difference (A - B): {difference_set}")