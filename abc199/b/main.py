
def solve(A,B,N):
    candidates = []
    for i in range(N):
        candidates.append(set(range(A[i],B[i]+1)))
    ans: set = set([])
    for i,c in enumerate(candidates):
        if i == 0:
            ans = c
        ans = ans & c
    return len(list(ans))

def main():
    N = int(input())
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    print(solve(A,B,N))



if __name__ == '__main__':
    main()