Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import Counter
n,m=map(int,input().split())
a=list()
for i in range(1,n+1):
  for j in range(1,m+1):
    a.append(i+j)
print(a)
counter = Counter(a)
print(counter)
mxcnt=0
mxcnts=list()
for number, cnt in counter.items():
  mxcnt=max(mxcnt, cnt)
for number, cnt in counter.items():
  if mxcnt == cnt:
    print(number,end=' ')
