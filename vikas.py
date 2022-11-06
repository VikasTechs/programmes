def addition(num):
    print(num)
def substraction(num1):
    print(num1)




print("1. add \n 2. sub")
option = int(input("SELECT OPTION >>>>>>"))
one = int(input("ENTER 1st YOUR NUMBER"))
two = int(input("ENTER 2nd YOUR NUMBER"))
num = one + two
num1 = one - two

if option==1:
    addition(num)
elif option==2:
    substraction(num1)
else:
    print("invalid")


