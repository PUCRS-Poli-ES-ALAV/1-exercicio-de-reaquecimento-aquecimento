def multSuc(x:int, y:int) -> int:
    if (y == 0): 
        return 0
    return x + multSuc(x, y-1)

def main():
    print ("4x6 =", multSuc(4, 6))

if __name__ == "__main__":
    main()
    