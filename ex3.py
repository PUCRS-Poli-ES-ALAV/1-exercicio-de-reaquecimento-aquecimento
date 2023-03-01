def sum_den(n:int) -> int:
    if (n == 0):
        return 0
    else:
        return 1/n + (sum_den(n-1))

def main():
    print ("Sum(1 -> 1/3) = ", sum_den(3))

if __name__ == "__main__":
    main()
    