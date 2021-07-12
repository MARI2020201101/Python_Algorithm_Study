Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,k=map(int,input().split())

num = max(n,k)
lists=[0]*(num+1)
#인덱스0=1, 이후 1부터.
for i in range(1,num+1):
  if i%2!=0:
    lists[i]=(i//2)+1
  else:
    lists[i]=(i//2)*10
print(lists[k]+lists[n])