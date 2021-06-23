Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #동전종류의 개수를 입력받는다
#만들어야하는 value를 입력받는다
#동전 종류를 입력받는다
#동전종류를 리스트에 저장한다. 리스트를 reverse한다
#리스트를 첫번째 부터 끝까지 돌린다.
#만약에 해당 list[i] 로 나누어진다면 -> value를 업데이트한다. cnt에 몫을 더한다.
#출력

n, target = map(int,input().split())
cnt=0
list=[0]*n
for i in range(n):
  list[i]=int(input())
list.reverse()

for i in range(n):
  cnt+=target//list[i]
  target=target%list[i]

print(cnt)
