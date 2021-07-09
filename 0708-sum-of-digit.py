Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def digit_sum(x):
  sum=0
  for xx in x:
    sum+=int(xx)
  return sum




n=int(input())
lists = list(input().split())
maxsum=0

maxnum=""
for a in lists:
  
  maxsum= max(digit_sum(a),maxsum)
  if maxsum == digit_sum(a): 
    maxnum=a


print(int(maxnum))