# if we were to have a dictionary 
# of a student's subject and score as key-value pairs
ashley = {
    "maths": 10,
    "english": 30,
    "programming": 50,
    "accounting": 40
}

james = {
    "maths": 20,
    "english": 60,
    "programming": 50,
    "accounting": 40
}

# introduction to functions
# the total mark function takes a students record
def total_mark(student):
    marks = []
    
    for subject, score  in student.items():
        marks.append(score)
        
    total_mark = sum(marks)
    
    return total_mark


def output(func, *args):
    for argument in args:
        print(f"Student's score is : {func(argument)}")
    
output(total_mark, james, ashley)
