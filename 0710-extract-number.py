Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

def makeNumber(strr):
  result=""
  for s in strr:
    if s.isdigit():
      result+=s
  return int(result)

def countFactor(num):
  cnt=0
  for n in range(1, int(num**(1/2))):  
    if num%n==0:
      cnt+=2
  if num**(1/2)==(math.floor(num**(1/2))):
    cnt+=1
  return cnt

strr=input()
num=makeNumber(strr)
print(num)
print(countFactor(num))
