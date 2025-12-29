lucky = 12
gues = 9

if gues < lucky - 2 :
    print("too low")
    
if gues > lucky + 2 :
    print("too high")
    
if gues == 12 :
    print("correct")
elif (gues >= lucky - 2) and (gues <= lucky + 2) :
    print("Almost There")
