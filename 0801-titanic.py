Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
people=list(map(int,input().split()))
people.sort()
cnt=0
p1=0
p2=n-1
while(p1<=p2):
  if people[p1]+people[p2]<=m:
    cnt+=1
    p1+=1
    p2-=1
  else:
    cnt+=1
    p2-=1
print(cnt)