import sys

def solve(listA: list, listB :list):
    work_with_two_men :int = pow(10, 5)
    a_min = min(listA)
    for i, b in enumerate(listB):
        if i == listA.index(a_min):
            continue
        work_with_two_men = min(max(a_min, b), work_with_two_men)
    work_with_one_man :int= pow(10, 5)
    for a, b in zip(listA, listB):
        work_with_one_man = min(a + b, work_with_one_man)
    return min(work_with_one_man, work_with_two_men)

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a , b = map(int, sys.stdin.readline().split(" "))
        A.append(a)
        B.append(b)
    ans = solve(A, B)
    print(ans)

if __name__ == '__main__':
    main()