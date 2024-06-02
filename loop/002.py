

student_heights =input("Input a list of student heights :").split(",")
student_numer=0
total_height=0

for height in student_heights:
    total_height=total_height+int(height)
    student_numer=student_numer+int(1)

print(total_height)
print(student_numer)