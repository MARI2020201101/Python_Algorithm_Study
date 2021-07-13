Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
n = int(input())
nums = list(input().split())

def reverse(x):
  x=x[::-1]
  return int(x)

def isPrime(x):  
  flag = True
  for i in range(2,(x+1)//2): 
    if x%i==0:
      flag = False
      break    
  return flag

for idx,n in enumerate(nums):
  nums[idx]=reverse(n)

decimals = list()
for n in nums:
  if isPrime(n)==True:
    decimals.append(n)
print(*decimals)
