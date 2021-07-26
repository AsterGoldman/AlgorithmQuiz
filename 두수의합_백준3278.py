import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
end = len(arr)-1
left, right = 0, end #left=0, right는 마지막 요소
count = 0
if not arr:
    print(0)
arr.sort()
flag =True          
while left<right:
    if arr[left]+arr[right] == x:
        count += 1
    elif arr[left]+arr[right]<x:
        left += 1
        continue
    right -=1
    
print(count)

