import sys
import numpy as np

def main():
    N = int(sys.stdin.readline())
    a : np.ndarray = np.fromiter(map(lambda s: int(s), sys.stdin.readline().split(" ")), dtype=int)
    divcount = 0
    while np.count_nonzero(a % 2) == 0:
        a = a // 2
        divcount += 1
    ans = divcount
    print(ans)


if __name__ == '__main__':
    main()