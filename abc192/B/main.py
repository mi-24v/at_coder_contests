import sys
import re

def main():
    # 1文字だけ | 偶数文字長 | 奇数文字長
    matcher = re.compile("^[a-z]$|^([a-z][A-Z])+$|^[a-z]([A-z][a-z])+$")
    S :str = sys.stdin.readline()
    ans = matcher.match(S) is not None
    if(ans):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()