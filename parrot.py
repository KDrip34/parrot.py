prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
#Giving them options to chose 
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
#While loop regulates whatever response you put in the computer 
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)	
