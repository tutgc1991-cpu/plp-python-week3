# Grade Reporter
# This program checks scores and reports grades.

scores = [72, 45, 90, 61, 38]

total = 0
passed = 0
failed = 0

for score in scores:
    total += score

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    if score >= 50:
        passed += 1
    else:
        failed += 1

    print("Score:", score, "Grade:", grade)

average = total / len(scores)

print("Total score:", total)
print("Average score:", average)
print("Number of students who passed:", passed)
print("Number of students who failed:", failed)