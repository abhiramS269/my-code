myList = []
a = int(input("Enter first num : "))
b = int(input("Enter last num  : "))

print("All positive numbers in the range : ")
for i in range(a, b):
    if i >= 0:
	    print(i, end = " ")