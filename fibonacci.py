def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old

if __name__ == "__main__":
    print(fib(10))
