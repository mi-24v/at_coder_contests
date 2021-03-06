import numpy as np
import copy

def sum_squad_np(l):
    total :int = 0
    l_sub = copy.deepcopy(l)
    l = np.array(l, dtype=np.int64)
    for _ in range(len(l) - 2): #FIXME 何回入れ替えたらいい?
        l_sub.append(l_sub.pop(0))
        l_sub_np = np.array(l_sub, dtype=np.int64)
        total += np.sum((l - l_sub_np) ** 2)
    return total

# 解説通り
def sum_squad(l : list, N: int):
    sum_l = pow(sum(l), 2)
    sum_r = sum(map(lambda x: pow(x,2), l))
    sum_squad = N * sum_r - sum_l
    return sum_squad

def main():
    N = int(input())
    A :list = list(map(int, input().split(" ")))
    ans = sum_squad(A, N)
    # ans = sum_squad_np(A)
    print(ans)

if __name__ == '__main__':
    main()