from temperature.celsius_to_fahrenheit import convert as ctof
from temperature.fahrenheit_to_celsius import convert as ftoc
from temperature.celsius_to_kelvin import convert as ctok

print("1. C to F")
print("2. F to C")
print("3. C to K")

choice = int(input("Choice: "))

temp = float(input("Enter temperature: "))

if choice == 1:
    print("Result:", ctof(temp))
elif choice == 2:
    print("Result:", ftoc(temp))
elif choice == 3:
    print("Result:", ctok(temp))