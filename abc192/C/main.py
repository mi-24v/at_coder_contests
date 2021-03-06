import sys

def kaprekar(x: int):
    if x == 0:
        return 0
    g_1 :int = int("".join(sorted(str(x), reverse=True)))
    g_2 :int = int("".join(sorted(str(x))))
    f = g_1 - g_2
    return f if f >= 0 else 0

def main():
    N, K = map(int, sys.stdin.readline().split(" "))
    a_i = N
    for _ in range(K):
        a_i = kaprekar(a_i)
    print(a_i)


if __name__ == '__main__':
    main()