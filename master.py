Total = 10000
Effort = 3

Days = Total // Effort
Rem_hours = Total % Effort
Months = Days // 30
Days = Days % 30
Years = Months // 12
Months = Months % 12

print(Years, "yrs", Months, "mnths", Days, "days", Rem_hours, "hrs")
