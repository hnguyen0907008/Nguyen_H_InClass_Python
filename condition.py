print ("Rule that govern the state of water")
current_temp = False #input temperature
while current_temp is False:
	current_temp = int(input("Enter a temperature:\n"))
	print("you input", current_temp)
	if (current_temp < 0 or current_temp == 0):
		print("Water is a solid as it's at or below freezing")
		current_temp = False
	elif (current_temp < 100):
		print("Water is liquid as it's above freezing and below boiling")
		current_temp = False
	elif (current_temp > 100 or current_temp == 100):
		print("Water is gas")
		current_temp = False
