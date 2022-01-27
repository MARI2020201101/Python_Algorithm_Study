Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import deque 
m,n=map(int,input().split())
a =tuple((idx,p) for idx,p in enumerate(list(map(int,input().split()))))
a=deque(a)
cnt=0
while True:
  x=a.popleft()
  if any(x[1]<b[1] for b in a):
    a.append(x)
  else:
    cnt+=1
    if x[0]==n:
      break
print(cnt)
