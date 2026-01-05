T = int(input())
for _ in range(T):
    stk = []
    VPS = True
    for char in input():
        if char == "(":
            stk.append(char)

        else:
            if stk:
                stk.pop()
            else:
                VPS = False
                break

    if stk:
        VPS = False

    print('YES' if VPS else 'NO')