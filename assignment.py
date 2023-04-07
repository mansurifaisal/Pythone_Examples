# Problem 3 solution

# enter your input

print("Number of classes held")
classes_held = int(input())

print("Number of classes attended")
classes_attended = int(input())

# Calculate the attendance percentage

attendance = classes_attended*100/classes_held
print(f'The attendance is {attendance}')

if attendance < 75:
    print("The Student is not allowed to sit in exam")
else:
    print("The student is allowed to sit in exam")

# Problem 4 solution

# Your input

print("Enter your marks")
marks = int(input())

if marks < 25:
    print("Your grade is F")
elif marks <= 45:
    print("Your grade is E")
elif marks <= 50:
    print("Your grade is D")
elif marks <= 60:
    print("Your grade is C")
elif marks <= 80:
    print("Your grade is B")
else:
    print("Your grade is A")