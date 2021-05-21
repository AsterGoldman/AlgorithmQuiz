import sys
n = int(sys.stdin.readline())
numbers = list(map(int , sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_result = -1e9
min_result = 1e9

def sol(i,res):
    global max_result, min_result, add, sub, mul, div
    if i == n:
        max_result = max(res, max_result)
        min_result = min(res, min_result)

    else:
        if add > 0:
            add -= 1
            sol(i+1, res + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            sol(i+1, res - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            sol(i+1, res * numbers[i])
            mul+= 1
        if div > 0:
            div -= 1
            sol(i+1, int(res / numbers[i]))
            div += 1

sol(1,numbers[0])
print(max_result)
print(min_result)


