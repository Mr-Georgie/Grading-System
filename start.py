# if we were to have a dictionary 
# of a student's subject and score as key-value pairs

ashley = {
    "maths": 10,
    "english": 30,
    "programming": 50,
    "accounting": 40
}

# we want to get a list 
# of all his scores from the dictionary above

#we create an empty list that will contain the students scores
marks = []

# we iterate over the dictionary to pick out each subjects score    
for subject, score  in ashley.items():
    marks.append(score)

    
total = sum(marks)
average = total / marks

print(f"Ashley's score is : {total}")