from utils import genfib


def solution():
    # Sum of the even fibonacci numbers that do not exceed 4 million
    high = 4000001
    fib = genfib()
    n = fib.next()
    acc = 0
    while n < high:
        if n % 2 == 0:
            acc += n
        n = fib.next()

    return acc


if __name__ == "__main__":
    print solution()
