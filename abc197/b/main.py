from typing import List

CELL = "."
OBSTACLE = "#"

class Field:
    width :int
    height :int
    field :List[List[str]]

    def __init__(self, width, height, field) -> None:
        self.width = width
        self.height = height
        self.field = field


def solve(field: Field, x, y) -> int:
    ans = -3 # 自身のカウント被り分を引いておく
    # left
    for next_y in range(y, -1, -1):
        if field.field[x][next_y] == OBSTACLE:
            break
        elif field.field[x][next_y] == CELL:
            ans += 1
    # right
    for next_y in range(y, field.width):
        if field.field[x][next_y] == OBSTACLE:
            break
        elif field.field[x][next_y] == CELL:
            ans += 1
    # down
    for next_x in range(x, -1, -1):
        if field.field[next_x][y] == OBSTACLE:
            break
        elif field.field[next_x][y] == CELL:
            ans += 1
    # up
    for next_x in range(x, field.height):
        if field.field[next_x][y] == OBSTACLE:
            break
        elif field.field[next_x][y] == CELL:
            ans += 1
    return ans


def main():
    H, W, X, Y = map(int, input().split(" "))
    field = []
    for _ in range(H):
        row = [char for char in input()]
        field.append(row)
    f = Field(W, H, field)
    ans = solve(f, X-1, Y-1)
    print(ans)

if __name__ == '__main__':
    main()