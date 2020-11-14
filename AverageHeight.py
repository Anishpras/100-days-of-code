student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
avg = 0
i = 0
for height in student_heights:
    total += height
    i += 1
avg = total / i

print(f"The average height is {avg} ")
