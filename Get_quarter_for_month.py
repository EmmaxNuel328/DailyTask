def get_quarter_for_month(month_number):
	if(month_number > 0 and month_number <= 3):
		return "is part of the first quarter"

	if(month_number > 3 and month_number <= 6):
		return "is part of the second quarter"

	if(month_number > 6 and month_number <= 9):
		return "is part of the third quarter"

	if(month_number > 9 and month_number <= 12):
		return "is part of the fourth quarter"

	if(month_number <= 0 or month_number > 12):
		return "INVALID INPUT"


user_input = int(input("Enter month number: "))
print("Month",user_input,get_quarter_for_month(user_input))


