
def translate_half_swaped(x: int, N: int) -> int:
    if x < N:
        return x+N
    else:
        return x-N

def swap(S:list, A:int, B:int) -> str:
    S[A], S[B] = S[B], S[A]
    return "".join(S)

def half_swap(S, N) -> str:
    return S[N:] + S[:N]

def solve(S, N, queries):
    half_swaped = False
    for q in queries:
        if half_swaped:
            A = translate_half_swaped(q["A"], N-1)
            B = translate_half_swaped(q["B"], N-1)
        else:
            A = q["A"]
            B = q["B"]
        if q["T"] == 1:
            S = swap(list(S), A, B)
        elif q["T"] == 2:
            half_swaped = not half_swaped
    if half_swaped:
        S = half_swap(S, N)
    return S

def main():
    N = int(input())
    S: str = input()
    Q = int(input())
    queries = []
    for _ in range(Q):
        T, A, B = map(int, input().split(" "))
        queries.append({
            "T" : T,
            "A" : A-1, # 1始まりなので変換
            "B" : B-1
        })
    print(solve(S, N, queries))

if __name__ == '__main__':
    main()