# Given three numbers a,b&m. write a program to calculate a power b % m.


def power_mod(a, b, m):
    if b == 0:
        return 1
    elif b % 2 == 0:
        result = power_mod(a, b // 2, m)
        return (result * result) % m
    else:
        return (a * power_mod(a, b - 1, m)) % m
a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
m = int(input("Enter the modulo (m): "))
print("Result of", a, "^", b, "%", m, "is:", power_mod(a, b, m))
