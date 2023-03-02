def rev_str(s: str) -> str: 
    if len(s) < 2:
        return s

    return s[-1] + rev_str(s[1:-1]) + s[0]

def main():
    s = "Testando!"
    print(s,"->",rev_str(s))
    print(rev_str(s) == s[::-1])

if __name__ == "__main__":
    main()
