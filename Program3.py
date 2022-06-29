num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

def compute_gcd(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

print("The H.C.F. is", compute_gcd(num1, num2))
print("Abhay Garg_01")
