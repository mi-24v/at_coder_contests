
def solve(total_count: int, total_charge: int):
    for x in range(total_count+1):
        y :float = (total_charge - 1000*total_count - 9000*x) / 4000
        if y.is_integer():
            y = int(y)
            z = total_count - x - y
            if x >= 0 and y >= 0 and z >= 0:
                return x, y, z
    return -1, -1, -1

def main():
    N, Y = tuple(map(lambda s: int(s), input().split(" ")))
    x, y, z = solve(N, Y)
    print("{} {} {}".format(x, y, z))




if __name__ == '__main__':
    main()