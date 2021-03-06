import math

def number_from_base(digits :str, b :int):
    if int(digits) == 0:
        return 0
    n :int = 0
    for i, digit in enumerate(digits):
        n += int(math.pow(b, i) * float(digit))
    return n

def check(arg :str, base :int, limit :int):
    if base <= 10: # int()の基数変換が有効なのは36までらしいが36いっぱいまで使うと重い
        value :int = int(arg, base)
    else:
        value :int = number_from_base(arg, base)
    return value <= limit

def main():
    X :str = input()
    M :int = int(input())
    sorted_X = sorted(X)
    d :int = int(sorted_X[len(sorted_X)-1])
    # bisect maxbase
    max_base :int
    right_edge :int = M * 2
    left_edge :int = d
    while right_edge - left_edge > 1:
        middle :int = left_edge + ( (right_edge-1) // 2 )
        if check(X, middle, M):
            left_edge = middle
        else:
            right_edge = middle
    max_base = left_edge
    ans = max_base - d
    print(ans)


if __name__ == '__main__':
    main()