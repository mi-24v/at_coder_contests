
def main():
    n = int(input())
    a = sorted(map(lambda s: int(s), input().split(" ")), reverse=True)
    alice_point = 0
    bob_point = 0
    for i, ai in enumerate(a):
        if i % 2 == 0:
            alice_point += ai
        else:
            bob_point += ai
    ans = alice_point - bob_point
    print(ans)


if __name__ == '__main__':
    main()