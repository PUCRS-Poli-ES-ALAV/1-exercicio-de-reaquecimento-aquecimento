def cartesian_product(lst, n):
    if n == 1:
        return lst
    
    return [let + next_lets \
                for next_lets in cartesian_product(lst, n - 1) \
                for let in lst]

def main():
    n = int(input("Enter n: "))
    lst = [chr(let) for let in range(65, 65 + n)]
    
    print (cartesian_product(lst, n))

if __name__ == "__main__":
    main()
