english_max = 75
science_max = 90
maths_max = 100

english =int(input("What is your english score "))
# english = 75
science = int(input("What is your science score "))
# science = 80 
maths = int(input("What is your maths score "))
#maths = 100

EP = (english / english_max) * 100

SP = (science / science_max) * 100

MP = (maths / maths_max) * 100

if (EP > 90) and (SP > 90) and (MP > 90) :
    print("Grade A")
    
elif (EP > 80) and (SP > 80) and (MP > 80) :
    print("Grade B")
    
elif (EP < 35) and (SP < 35) and (MP < 35) :
    print("Fail")
    
else:
    print("Avergae")
