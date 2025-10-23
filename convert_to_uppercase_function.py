def convert_to_uppercase(prompt):
	if prompt == prompt.upper():
		raise ValueError ("Prompt already in capital letter!!!")
	expected = prompt.upper()
	return expected