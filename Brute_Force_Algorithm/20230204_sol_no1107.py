# question URL: https://www.acmicpc.net/problem/1107

N = int(input())
M = int(input())

# 사용할 수 있는 리모컨 번호 리스트
if M:
    ar = list(map(int, input().split())) # 고장난 키가 있을 때
else:
    ar = [] # 고장난 키가 없을 때

ch = 100

# +/-로만 이동할 때
cnt_min = abs(ch - N)

# 번호키와 +/-를 같이 쓸 때
for i in range(1000001):
    tmp = str(i)

    for j in range(len(tmp)):

        # 해당 번호로 번호를 사용하여 갈 수 있는지 파악
        if int(tmp[j]) in ar:
            break

        else:
            # 해당 번호로 이동한 후에 남은 나머지를 +/-로 이동한다
            if j == len(tmp) - 1:
                cnt_min = min(cnt_min, abs(int(tmp) - N) + len(tmp))


print(cnt_min)
