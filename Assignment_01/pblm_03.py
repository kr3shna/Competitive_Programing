# Given a string S,write a program to reverse it


def reverse_string_recursive(S):
    if len(S) == 0:
        return S
    else:
        return reverse_string_recursive(S[1:]) + S[0]
S = input("Enter a string: ")
print("Reversed string:", reverse_string_recursive(S))
