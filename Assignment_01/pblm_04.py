# Given a number N,write a program to calculate Fibonacci(N)

def fibonacci(N):
    if N <= 1:
        return N
    else:
        return fibonacci(N-1) + fibonacci(N-2)
N = int(input("Enter a number: "))
print("Fibonacci of", N, "is", fibonacci(N))

