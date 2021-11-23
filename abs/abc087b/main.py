import sys

def main():
    a, b, c, x = tuple(map(int, sys.stdin.readlines()))
    ans = 0
    for ai in range(a+1):
        for bi in range(b+1):
            # 500円の枚数と100円の枚数が決まった時点で50円の枚数も確定する
            rest = x - 500 * ai - 100 * bi
            ans += 1 if rest >= 0 and rest//50 <= c else 0
    print(ans)

if __name__ == '__main__':
    main()