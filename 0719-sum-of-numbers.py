Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,target=map(int,input().split())
lists=list(map(int,input().split()))
cnt=0
for i in range(len(lists)): 
  temp=target 
  for j in range(i, len(lists)):  
    temp=temp-lists[j]
    if temp==0:
      cnt+=1
      break
    if temp<0:
      break

print(cnt)