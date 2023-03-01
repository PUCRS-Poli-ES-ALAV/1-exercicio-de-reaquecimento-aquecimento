def cartesian_product(lst, n):
    if n == 1:
        return lst
    return [x + y for y in cartesian_product(lst, n - 1) for x in lst]

def main():
    n = int(input("Enter n: "))
    lst = [chr(x) for x in range(65, 65 + n)]
    
    print (cartesian_product(lst, n))

if __name__ == "__main__":
    main()
