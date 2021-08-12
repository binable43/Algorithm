#BOJ_2960
#에라토스테네스의 체

n, k = map(int, input().split())

a = [False for _ in range(n+2)]
temp = 0


for i in range(2, n+1):
    if a[i] == False:
        for j in range(i, n+1, i):
            if a[j] == False:
                a[j] = True
                temp += 1

            if temp == k:
                print(j)
                break
