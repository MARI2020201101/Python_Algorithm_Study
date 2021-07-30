Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
players = list()


for i in range(n):
  a,b=map(int,input().split())
  players.append([a,b])

mx=0
cnt=0
players.sort(reverse=True)
for p in players:
  if mx<p[1]:
    cnt+=1
    mx=p[1]
print(cnt)