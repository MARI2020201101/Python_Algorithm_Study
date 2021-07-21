Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def move(gotgam,r,d,k):
  n=len(gotgam)
  lists=[0]*n
  if d==0:
    for i in range(n):
      lists[(i-k)%n]=gotgam[r][i]
    gotgam[r]=lists
  else:
    for i in range(n):
      lists[(i+k)%n]=gotgam[r][i] 
    gotgam[r]=lists
  return gotgam

def sandglass(gotgam):
  n=len(gotgam)
  s=0
  e=n
  sum=0
  for i in range(n):
    if i<n//2:
      for j in range(s,e):
        sum+=gotgam[i][j]
      s+=1
      e-=1
    else:
      for j in range(s,e):
        sum+=gotgam[i][j]
      s-=1
      e+=1
  return sum

n=int(input())
gotgam=[list(map(int,input().split())) for i in range(n)]
m=int(input())
for i in range(m):
  r,d,k=map(int,input().split())
  gotgam=move(gotgam,r-1,d,k)
print(sandglass(gotgam))