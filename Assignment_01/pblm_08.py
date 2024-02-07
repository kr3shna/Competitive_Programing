# Given a number in decimal, write a program to print its binary form


def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return decimal_to_binary(decimal // 2) + str(decimal % 2)

decimal = int(input("Enter a decimal number: "))
print("Binary representation:", decimal_to_binary(decimal))
