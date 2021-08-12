#BOJ_3079
#입국심사

import sys

input_list = input().split()

N = int(input_list[0])
M = int(input_list[1])

times = []
time_max = 0

for _ in range(N):
    input_list_2 = sys.stdin.readline().split()
    input_num = int(input_list_2[0])
    times.append(input_num)
    if input_num > time_max:
        time_max = input_num

left = 1
right = time_max * M
ans = right

while left <= right:
    mid = (left+right)//2
    people = 0
    for i in range (N):
        people += mid//times[i]

    if people < M:
        left = mid+1
    else:
        right = mid-1
        if mid < ans:
            ans = mid

print(ans)

