def ackerman(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1)
    elif m > 0 and n > 0:
        return ackerman(m - 1, ackerman(m, n - 1))

def main():
    print ("m=0, n=6 ->",ackerman(0, 6))
    print ("m=4, n=0 ->",ackerman(4, 0))
    print ("m=3, n=2 ->",ackerman(3, 2))

if __name__ == "__main__":
    main()