Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
nums = dict()
for i in range(n):
  x,y=map(int,input().split())
  nums[x]=y
maxs=0
def dfs(times,sums):
  global maxs
  if(times>m):
    return
  else: 
    maxs=max(maxs,sums)
    for a,b in enumerate(nums):
      dfs(times+a,sums+b)

dfs(0,0)
