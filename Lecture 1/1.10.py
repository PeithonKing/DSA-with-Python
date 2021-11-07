while True:
	age = input("\nEnter your age: ")
	if age.lower() == "quit": break
	else: age = int(age)
	if age < 18:
		print("Only adults are allowed!")
	elif age < 61:
		print("Ticket costs rupees 50.")
	else: print("Ticket costs rupees 25.")
