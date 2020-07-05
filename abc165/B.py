import math

def read_input():
    return int(input())

def solve(X):
    n = 0
    balance = 100.0
    while balance < X:
        balance = math.floor(balance * 1.01)
        n += 1
    ans = n
    print(ans)

def main():
    X = read_input()
    solve(X)


if __name__ == "__main__":
    main()
