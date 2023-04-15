def main():
    N = int(input())
    S = input()
    ans: bool = "o" in S and "x" not in S
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
