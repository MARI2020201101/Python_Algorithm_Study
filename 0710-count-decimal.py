Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def issosu(n):
  res = False
  if n==2:
    return True
  for i in range(2,n):
    if n%i==0:
      break
    if i==n-1 and n%i!=0:      
      res=True
  return res

n = int(input())
result = 0
for i in range(2,n):
  if issosu(i)==True:
    result+=1
print(result)