from datetime import datetime

name = input("\nPlease, write your name: ")
age = int(input("\nPlease, enter your age: "))

thisYear = datetime.now().year
be100in = thisYear + (100 - age)

print(f"\n\nDear {name}, you'll be 100 in {be100in}")
