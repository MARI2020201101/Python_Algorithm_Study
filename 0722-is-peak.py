Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isPeak(n,square, x, y):
  nx = [1,0,-1,0]
  ny = [0,1,0,-1]
  mx = square[x][y]
  for i in range(4):  
    if x+nx[i]>=n or y+ny[i]>=n or x+nx[i]<0 or y+ny[i]<0: 
      continue
    else:
      mx=max(mx, square[x+nx[i]][y+ny[i]])
  if mx == square[x][y]:
    return True
  else:
    return False

n=int(input())
square = [list(map(int,input().split())) for i in range(n)]

cnt=0
for i in range(n):
  for j in range(n):
    if isPeak(n,square,i,j)==True:
      cnt+=1
print(cnt)
