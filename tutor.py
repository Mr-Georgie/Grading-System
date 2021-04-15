# first we ask the user to input the student's scores
print("Please enter the student scores for the subjects below:")

# save the user input for the appropriate subject
maths = int(input("Maths: "))
english = int(input("English: "))
programming  = int(input("Programming: "))
accounting = int(input("Accounting: "))


# we assign the variables to their appropriate subject in the dictionary
student = {
    "Maths": maths,
    "English": english,
    "Programming": programming,
    "Accounting": accounting
}


# an empty list that will contain the student's mark
student_marks = []

# the iteration
for score  in student.values():

    #the collection
    student_marks.append(score)

# get the sum of scores
total_score = sum(student_marks)

# get the average score
average = total_score / len(student_marks)

# check if the average score is below/ above 50 to give remark
if average < 50:
    remark = "FAIL"
else:
    remark = "PASS"

# print out the information for the student parent to see 😁
print("====================")
print("Student's result:")
print(f"Total: {total_score}; Average: {average}%; Remark: {remark}")
