from calc import *
def get_nums () :
    nums = []
    while (True) :
        try :
            num = int(input("enter a number: ---> "))
        except (ValueError) :
            break
        nums.append(num)

    return nums

nums = get_nums()

print(nums)

opration = input("opration : + __ - __ * __ / ---> ")

if opration == '+' :

    res = addition(nums)
    print(res)

elif opration == '-' :

    res = subtraction(nums)
    print(res)

elif opration == '*' :

    res = multiplication(nums)
    print(res)

elif opration == '/' :

    res = division(nums)
    print(res)


