# Given a number N, write a program to print numbers from 1 to N.

def print_numbers(N):
    if N > 0:
        print_numbers(N - 1)
        print(N)
N = int(input("Enter a number: "))
print("Numbers from 1 to", N, "are:")
print_numbers(N)
