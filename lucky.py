lucky = 12
gues = 10

if gues < lucky - 2 :
    print("too low")
elif gues > lucky + 2 :
    print("too high")
elif gues == lucky :
    print("correct")
else :
    print("Almost There")

