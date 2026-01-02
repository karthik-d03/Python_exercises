# school conducts a exam in subjects english, science and maths. maximum marks for each subjects is 100.

# Get marks scored by a student in these subjects and grade the student according to following criteria.
#   Grade A : if total marks is > 90%
#   Grade B : if total marks is > 80%
#   Average : if if student as not failed
#   Grade A : if total marks is < 35 %
        


max = 100 * 3
eng = 45
math = 56
sci = 67

percent = (eng + math + sci) / 3

if percent > 90 :
    print("Grade A")
    
if (percent > 80) and (percent <= 90) :
    print("grade B")
    
if (percent <= 80) and (percent >= 35) :
    print("Avg")
    
if percent < 35 :
    print("Fail")
