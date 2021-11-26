import numpy as np


WORDS = ["dream", "dreamer", "erase", "eraser"]

def solve(target :str):
    checked = np.full(shape=len(target)+1, fill_value=False)
    checked[0] = True
    for i in range(len(target)+1):
        for w in WORDS:
            in_check_index = i - len(w)
            in_check = target[in_check_index:in_check_index+len(w)]
            if i >= len(w) and \
                    checked[in_check_index] and \
                    in_check == w:
                checked[i] = True
    return checked[len(target)]

def main():
    S = input()
    ans = solve(S)
    if ans:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()