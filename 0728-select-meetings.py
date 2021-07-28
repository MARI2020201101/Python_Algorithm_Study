Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
meetings=list()
for i in range(n):
  a,b=map(int,input().split())
  meetings.append([a,b])
meetings.sort()
print(meetings)
mx=0

check=[0]*n

def promising(start,meetings,j):
  if start<=meetings[j][0] and check[j]!=1:
    return True
  return False


for i in range(len(meetings)):
  cnt=1
  start=meetings[i][1]  
  check[i]=1
  for j in range(i,len(meetings)):
    while(promising(start,meetings,j)):
      cnt+=1
      start=meetings[j][1]
      check[j]=1
  mx=max(mx,cnt)
print(mx)


  