def addition(num):
    print(num)
def substraction(num1):
    print(num1)
def multiply(num2):
    print(num2)
def division(num3):
    print(num3)
print("1. add \n 2. sub \n 3. mul \n 4. div")
option = int(input("SELECT OPTION >>>>>>"))
one = int(input("ENTER 1st YOUR NUMBER"))
two = int(input("ENTER 2nd YOUR NUMBER"))
num = one + two
num1 = one - two
num2 = one * two
num3 = one / two
if option==1:
    addition(num)
elif option==2:
    substraction(num1)
elif option==3:
    substraction(num2)
elif option==4:
    substraction(num3)
else:
    print("invalid")




