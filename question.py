# a = int(input("enter the num1 :"))
# b = int(input("enter the num2 :"))
# c = int(input("enter the num3 :"))

# if a > b and a > c:
#     print("a is greater")
# elif b > c and b > a:
#     print("b is greater")
# else:
#     print("c is greater")

# a = int(input("enter the num1 :"))
# b = int(input("enter the num2 :"))
# c = int(input("enter the num3 :"))

# if a < b and a < c:
#     print("a is smaller")
# elif b < c and b < a:
#     print("b is smaller")
# else:
#     print("c is smaller")


a = int(input("enter the num1 :"))
b = int(input("enter the num2 :"))
c = int(input("enter the num3 :"))

if (a>b and a<c)  or (a<b and a>c):
    print("a is middle")
elif (b>a and b<c) or (b<a and b>c):
    print("b is middle")
else:
    print("a is middle")
    


