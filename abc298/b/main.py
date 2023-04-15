import numpy
import numpy as np


def parse(matrix_rows):
    matrix = []
    for _ in range(matrix_rows):
        matrix_cols = list(map(int, input().split(" ")))
        matrix.append(matrix_cols)
    return np.asarray(matrix, dtype=np.int32)


def solve(a: np.ndarray, b: numpy.ndarray):
    test_result = []
    for i in range(4):
        rotated = np.rot90(a, -i)
        testament = b - rotated
        test_result.append(np.all(testament >= 0))
    return True in test_result


def main():
    N = int(input())
    A = parse(N)
    B = parse(N)
    ans: bool = solve(A, B)
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
