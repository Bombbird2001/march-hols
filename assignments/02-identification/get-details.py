name = input("What is your name? ")

# If length of name is greater than 20,
# print something
if len(name) > 20:
	print("That's a long name")


while True:
	try:
		age = int(input("What is your age? "))
		break
	except:
		print("Please input a valid integer!")
if age < 10:
	print("Smol")
elif age < 20:
	print("Big boi")
else:
	print("Big big boi")
# If age is less than 10, print "Smol"
# ELse if age is between 10 and 20, print "Big boi"
# Else, print "Big big boi"


while True:
	try:
		coolness = float(input("Rate your coolness out of 100.0 "))
		break
	except:
		print("Please input a valid number!")
if coolness > 100.0:
	print("Kek u 2 cool 4 me")
# If coolness is more than 100.0, just print some error



# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool
print("My name is", name + ",", "I am", age, "and I'm Really Cool")

