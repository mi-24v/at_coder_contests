
def solve(points):
    conditions :list[bool] = []
    for i, point in enumerate(points):
        if i == 0: continue
        t_i, x_i, y_i = point
        t_before, x_before, y_before = points[i - 1]
        dt = t_i - t_before
        distance = abs(x_i - x_before) + abs(y_i - y_before)
        if dt >= distance and distance % 2 == dt % 2:
            conditions.append(True)
        else:
            conditions.append(False)
    return all(conditions)

def main():
    N = int(input())
    points :list[tuple[int]] = [(0,0,0)]
    for _ in range(N):
        points.append(tuple(map(int, input().split(" "))))
    if solve(points):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
