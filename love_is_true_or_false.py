def is_love_true_or_false(prompt1,prompt2):
	if prompt1 % 2 == 0 and prompt2 % 2 != 0 : 
		return True
	if prompt1 % 2 != 0 and prompt2 % 2 == 0 : 
		return True
	if prompt1 % 2 == 0 and prompt2 % 2 == 0 : 
		return False
	if prompt1 % 2 != 0 and prompt2 % 2 != 0 : 
		return False



#first_input = int(input("Enter a number"))
#second_input = int(input("Enter a number"))
#print(number_of_petal(first_input,second_input))