# 🚨 Don't change the code below 👇
student_max=0

student_scores = input("Input a list of student scores ").split(",")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n]>student_max:
      student_max=student_scores[n]
print(f"the highest score is{student_max}")