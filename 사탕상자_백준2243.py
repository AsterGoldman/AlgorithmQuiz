import sys
import heapq


input = sys.stdin.readline

def two(a:int, b:int):
    ans = candy[b-1]
    print(ans)
    candy.remove(b)
    
def three(a:int ,b:int, c:int):
    if c>0:
        for _ in range(c):
            heapq.heappush(candy, b)
    elif c<0 and candy.count(b)>=-c:
        for _ in range(-c):
            candy.remove(b)

candy = list()
arr = []

n = int(input())
while n!=0:
    n -= 1
    arr =  list(map(int, input().split()))
    if arr[0]==1:
        two(arr[0],arr[1])

    if arr[0]==2:
        three(arr[0],arr[1],arr[2])


print(candy)
