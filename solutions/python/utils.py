def genfib():
    # Fibonacci generator. Be careful to not consume the entire thing!
    a, b = 0, 1

    while True:
        yield a+b
        a, b = b, a+b


def fib(n):
    gen = genfib()
    return list(gen.next() for i in range(n))

if __name__ == "__main__":
    print fib(10)
