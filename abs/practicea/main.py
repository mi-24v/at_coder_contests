import sys

def main():
    a :int = int(sys.stdin.readline())
    b, c= tuple(map(lambda s: int(s), sys.stdin.readline().split(" ")))
    s :str = sys.stdin.readline()
    ans = " ".join([str(a+b+c), s])
    print(ans, end="")


if __name__ == '__main__':
    main()