Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
square=[list(map(int,input().split())) for i in range(n)]
s=e=n//2
sum=0

for i in range(n):
  for j in range(s,e+1):
    sum += square[i][j]
  if i<(n//2):
    s-=1
    e+=1

  else:
    s+=1
    e-=1
  
print(sum)