lucky = 12
gues = 10

if gues < lucky - 2 :
    print("too low")
elif gues > lucky + 2 :
    print("too high")
elif gues == 12 :
    print("correct")
else :
    print("Almost There")
