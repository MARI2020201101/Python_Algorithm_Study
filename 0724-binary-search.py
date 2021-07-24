Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
a=list(map(int,input().split()))
start=0
end=n-1

a.sort()
while(True): 
  mid=(start+end)//2 
  if m==a[mid]:
    break
  elif m>a[mid]:
    start=mid+1
  else:
    end=mid-1
  

print(mid+1)
