def F(n:int) -> int:
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    else: 
        return 2 * F(n-1) + 3 * F(n-2)

def main():
    print ("F(5) =", F(5))

if __name__ == "__main__":
    main()
    