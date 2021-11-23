"""
find the nth number in the fibonacci sequence using recursion
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Enter a number: "))
    print(fibonacci(n))

__name__ == "__main__" and main()
