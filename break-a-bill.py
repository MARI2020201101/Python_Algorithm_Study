Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
coin=list(map(int,input().split()))
money=int(input())
coin.sort(reverse=True)
cnt=0
def dfs(money,i):
  global cnt
  if money==0 or i==n:
    print(cnt)
  elif(money>=coin[i]):
    cnt+=1
    money=money-coin[i]
    dfs(money,i)
  else:
    dfs(money,i+1)

dfs(money,0)
