# Given an array and number, count all occurrences of that number in the array



def count_occurrences(arr, num):
    if not arr:
        return 0
    elif arr[0] == num:
        return 1 + count_occurrences(arr[1:], num)
    else:
        return count_occurrences(arr[1:], num)

arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
num = int(input("Enter the number to count occurrences: "))
print("Number of occurrences of", num, "in the array:", count_occurrences(arr, num))
