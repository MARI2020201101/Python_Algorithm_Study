Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
a = list()
for i in range(n):
  print(a)
  num=int(input())
  if a and num==0:
    a.pop()
  else : a.append(num)

if len(a)==0: 
  print(0)
else:   
  print(sum(a))
