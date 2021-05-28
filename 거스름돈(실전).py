# 금액

n = int(input())


# 화폐단위

coin = [500, 100, 50, 10]

# 횟수

count = 0

# 거슬러 주는 방법

for i in coin:
    count += n // i
    n %= i
    if n == 0:
        break

print(count)