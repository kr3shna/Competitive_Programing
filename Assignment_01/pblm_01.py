# Given a number N,write a program to calculate factorial(N).

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
N = int(input("Enter a number: "))
print("Factorial of", N, "is", factorial(N))
