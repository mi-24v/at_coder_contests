import sys

def main():
    a ,b = tuple(map(lambda s: int(s), sys.stdin.readline().split(" ")))
    ans = "Even" if (a * b) % 2 == 0 else "Odd"
    print(ans)


if __name__ == '__main__':
    main()