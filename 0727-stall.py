Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check(mid):  
  cnt=1
  ep=points[0]
  for i in range(1,n):
    if points[n]-ep>=mid:
      cnt+=1
      ep=points[i]
  return cnt
  
    
n,c=map(int,input().split())
points = [int(input()) for _ in range(n)]
points.sort()
lt=1
rt=points[n-1]
while lt<=rt:
  mid=(lt+rt)//2
  if check(mid)>=c:
    res=mid
    lt=mid+1
  else:
    rt=mid-1
print(res)