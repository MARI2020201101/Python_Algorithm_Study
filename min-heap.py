Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import heapq as hq

a=[]
while True:
  n=int(input())
  if n==-1:
    break
  if n==0:
    if len(a)==0:
      print(-1)
    else: print(hq.heappop(a))
  else:
    hq.heappush(a,n)