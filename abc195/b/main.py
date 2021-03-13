import math

# 最小1個1(g) * 最大W=1(kg)で合計できる最大1000*1000(個)
MAX_COUNT = 1 * 1000 * 1000
MIN_COUNT = 0

def search(A :int, B :int, W :int):
    current_minimum = MAX_COUNT
    current_maximum = MIN_COUNT
    for orange_count in range(MAX_COUNT):
        if orange_count*A <= 1000*W <= orange_count*B:
            current_minimum = min(current_minimum, orange_count)
            current_maximum = max(current_maximum, orange_count)
    if current_maximum == 0:
        return "UNSATISFIABLE"
    else:
        return "{} {}".format(current_minimum, current_maximum)

def solve(A :int, B :int, W :int):
    minimum = math.ceil(1000 * W / B)
    maximum = math.floor(1000 * W / A)
    if minimum > maximum:
        return "UNSATISFIABLE"
    else:
        return "{} {}".format(minimum, maximum)

def main():
    A, B, W = map(int, input().split(" "))
    print(solve(A, B, W))


if __name__ == '__main__':
    main()
