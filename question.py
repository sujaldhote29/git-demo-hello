a = int(input("enter the num1 :"))
b = int(input("enter the num2 :"))
c = int(input("enter the num3 :"))

if a > b and a > c:
    print("a is greater")
elif b > c and b > a:
    print("b is greater")
else:
    print("c is greater")
