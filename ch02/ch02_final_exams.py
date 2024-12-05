""" 挑戰題 """
for i in range(100,1000):
    if (i % 5 == 3) and (i % 7 == 2) and (i % 3 == 1):
        print(i)


# 100≤105k+58≤999     
k = 1
ans = 100
while True:
    ans = 105 * k + 58
    if ans > 999:
        break
    print(ans)
    k += 1
