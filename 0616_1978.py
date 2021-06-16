Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isPrime(n):
  for i in range(2,n):
    if n%i==0: 
      return False
    return True

cnt=0
len = int(input())

arr = list(map(int,input().split())) 
for k in range(len):
  n = arr[k]
  if isPrime(n):
    cnt+=1
print(cnt)