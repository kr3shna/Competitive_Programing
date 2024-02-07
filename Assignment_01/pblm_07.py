# Given three numbers n,r & m,write a program to calculate nCr%m


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nCr_mod_m(n, r, m):
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    return (numerator // denominator) % m

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
m = int(input("Enter the value of m: "))
print("nCr % m is:", nCr_mod_m(n, r, m))
