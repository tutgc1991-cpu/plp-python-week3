# Bug Hunt
# This program demonstrates how a while loop stops.

number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("The loop stopped when number became:", number)
print("The total is:", total)