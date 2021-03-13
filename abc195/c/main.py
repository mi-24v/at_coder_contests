
def solve(max_number :int):
    comma_count = 0
    if max_number < 1000:
        return comma_count
    max_digits = len(str(max_number))
    comma_delta = 0
    for i in range(max_digits):
        comma_count += comma_delta * (pow(10,(i+1)) - pow(10,i))
        if i % 3 == 2:
            comma_delta += 1 # 3桁増えるごとにコンマ1個増える
    # if max_digits % 3 == 2:
    #     comma_delta += 1
    comma_count += comma_delta * (max_number - pow(10, max_digits) + 1)
    return comma_count

def main():
    N = int(input())
    print(solve(N))

if __name__ == '__main__':
    main()