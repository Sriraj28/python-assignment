student = {
    "name": "Yatharth",
    "age": 19
}

student["branch"] = "CSE"
print("Updated Dictionary:", student)

student.pop("age")
print("After Removing Age:", student)

extra = {"year": "FY"}
merged = {**student, **extra}
print("Merged Dictionary:", merged)