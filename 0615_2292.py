Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
1(1)
2,3,4,5,6,7(6)
8,9,10,11,12,13,14,15,16,17,18,19(12)
20,....37(18)
38,....61(24)

[1,7,19,37,61...]
f(n) = f(n-1)+(6n)
'''

def func(k):
  if k==0:
    return 1
  return func(k-1) +6*k


n=[]
N=int(input())

for i in range((N//6)+1):
  n.append(func(i))

print(*n)
