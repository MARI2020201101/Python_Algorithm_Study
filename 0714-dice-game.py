Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def cal(a,b,c):
  result = 0
  if a==b and a==c and b==c:
    result = 10000+(a*1000)
  elif a==b:
    result = 1000 + (a*100)
  elif a==c:
    result = 1000 + (a*100)
  elif b==c:
    result = 1000 + (b*100)
  else:
    mx=max(a,b)
    if max(b,c)>mx:
      mx=max(b,c)
    elif max(a,c)>mx:
      mx=max(a,c)
    result = mx*100
  return result

n=int(input())
lists=list()
for i in range(n):
  a,b,c=map(int,input().split())
  lists.append(cal(a,b,c))
print(max(lists))