# Given two numbers a and b, calculate GCD(a,b)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
print("GCD of", a, "and", b, "is:", gcd(a, b))
