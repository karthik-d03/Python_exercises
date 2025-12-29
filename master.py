Total = 10000
#Effort = 6
Effort = int(input("what is your daily effort? "))

Days = Total // Effort
Rem_hours = Total % Effort
Months = Days // 30
Rem_Days = Days % 30
Years = Months // 12
Rem_Months = Months % 12

print(Years, "yrs", Rem_Months, "mnths", Rem_Days, "days", Rem_hours, "hrs")
