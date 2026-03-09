t1 = tuple(map(int, input("Enter tuple elements: ").split()))

print("Tuple:", t1)
print("First Element:", t1[0])

nested = (t1, ("Python", "Lab"))
print("Nested Tuple:", nested)

print("Repeated Tuple:", t1 * 2)

t2 = (100, 200)
print("Concatenated:", t1 + t2)