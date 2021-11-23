import sys


def main():
    n = int(input())
    d = sorted(set(map(int, sys.stdin.readlines())), reverse=True)
    ans = len(d)
    print(ans)

if __name__ == '__main__':
    main()