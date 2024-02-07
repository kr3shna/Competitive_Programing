# Given a number, calculate the sum of its digits

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
