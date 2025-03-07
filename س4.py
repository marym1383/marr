a=float(input("enter num1:"))
b=float(input("enter num2:"))
c=float(input("enter num3:"))
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("yes")
else:
    print("no")
