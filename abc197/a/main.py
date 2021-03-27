from collections import deque

def main():
    S :deque = deque([char for char in input()])
    first :str = S.popleft()
    S.append(first)
    print("".join(S))



if __name__ == '__main__':
    main()
