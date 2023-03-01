def fib(n: int) -> int:
    if n < 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)

def main():
    for i in range(10):
        print(fib(i))

if __name__ == "__main__":
    main()