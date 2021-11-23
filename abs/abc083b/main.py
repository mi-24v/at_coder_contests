
def sum_digits(x: int):
    sum = 0
    while 0 < x:
        sum += x % 10
        x = x // 10
    return sum

def main():
    n, a, b = tuple(map(lambda s: int(s), input().split(" ")))
    ans = 0
    for i in range(1, n+1):
        sums = sum_digits(i)
        ans += i if a <= sums <= b else 0
    print(ans)


if __name__ == '__main__':
    main()