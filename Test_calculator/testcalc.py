a = float(input("First number "))
what = input("What action do you make? ")
b = float(input("Second number "))

if what == "+":
	print(a + b)
elif what == "-":
	print(a - b)
elif what == "*":
	print(a * b)
elif what == "/":
	print(a / b)
else:
	print("Invalid")

input()
