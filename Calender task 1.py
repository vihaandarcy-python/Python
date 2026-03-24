from datetime import date, time, datetime

#calling the today
#function of data class
today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\nCurrent Date and time is", now)

#printing date's componenets
print("\nDate componenets", today.year, today.month, today.day)
