Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= dict()
b= dict()
s1=input()
s2=input()
for s in s1:
  if s in a:
    a[s]+=1
  else: a[s]=1

for s in s2:
  if s in b:
    b[s]+=1
  else: b[s]=1

if a==b:
  print('YES')
else: print('NO')