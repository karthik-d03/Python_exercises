def divide (num, den):
    quot = num // den
    rem = num % den
    return quot, rem
    
total = 10000
effort = 3

#days = total // effort
#hours = total % effort
days, hours = divide(total, effort)

#months = days // 30
#days = days % 30
months, days = divide(days, 30)

#years = months // 12
#months = months % 12
years, months = divide(months, 12)

print(years, "yrs", months, "mnths", days, "days", hours, "hrs")
