


def main():
    A,B,C = map(int, input().split(" "))
    ans: bool = pow(A, 2) + pow(B, 2) < pow(C, 2)
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()