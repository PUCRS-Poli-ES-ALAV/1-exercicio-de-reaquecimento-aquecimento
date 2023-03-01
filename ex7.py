def sum_arr(ar:list[int], n=0) -> int:
    if (len(ar) == n):
        return 0 
    else:
        return ar[n] + sum_arr(ar,n+1)

def mult_arr(ar:list[int], n=0) -> int:
    if (len(ar) == n):
        return 1 
    else:
        return ar[n] * mult_arr(ar,n+1)

def main():
    array = [1,2,3,4,5]
    print ("Array:",array)

    print ("Sum:", sum_arr(array))
    print ("Mult:", mult_arr(array))

if __name__ == "__main__":
    main()
    