
def nat_succ_sum(x:int, y:int) -> int:
    if (y == 0):
        return 0     
    elif (x == 0):
        return 1 + nat_succ_sum(x, y-1)
    else:
        return 1 + nat_succ_sum(x-1, y)

def main():
    print ("9+4 =",nat_succ_sum(9, 4))

if __name__ == "__main__":
    main()

