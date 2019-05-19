# Python 3
import sys

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    #a, b = map(int, input().split())
    input = sys.stdin.read()
    tokens = input.split()
    a = int(tokens[0])
    b = int(tokens[1])
    print(sum_of_two_digits(a, b))