max = 100 * 3
eng = 75
math = 75
sci = 75

percent = (eng + math + sci) / 3

if percent > 90 :
    print("Grade A") 
elif (percent > 80) :
    print("grade B")
elif percent < 35 :
    print("Fail")
else :
    print("Avg")
