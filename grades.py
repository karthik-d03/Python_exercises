max = 100 * 3
eng = 85
math = 85
sci = 85

percent = (eng + math + sci) / 3

if percent > 90 :
    print("Grade A") 
elif (percent > 80) :
    print("grade B")
elif (percent >= 35) :
    print("Avg")
elif percent < 35 :
    print("Fail")
