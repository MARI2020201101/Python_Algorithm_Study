Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
moneys = list()
days = list()
for i in range(n):
  a,b=map(int,input().split())
  days.append(a)
  moneys.append(b)
maxs=0
def dfs(idx,day,sums):
  global maxs
  if(day>=n or idx==n):
    return
  else:
    maxs=max(maxs,sums)
    dfs(idx+1,day+days[idx],sums+moneys[idx])
    dfs(idx+1,day,sums)

dfs(0,0,0)
print(maxs)