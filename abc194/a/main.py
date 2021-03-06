
def main():
    A, B = map(int, input().split(" "))
    milk_solids = A + B
    if milk_solids >= 15 and B >= 8:
        ans = 1
    elif milk_solids >= 10 and B >= 3:
        ans = 2
    elif milk_solids >= 3:
        ans = 3
    else:
        ans = 4
    print(ans)

if __name__ == '__main__':
    main()
