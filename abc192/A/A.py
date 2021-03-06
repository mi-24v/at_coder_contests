import sys

def main():
    X = int(sys.stdin.readline())
    reminder = X % 100
    ans = 100 - reminder if reminder != 0 else 100
    print(ans)

if __name__ == '__main__':
    main()