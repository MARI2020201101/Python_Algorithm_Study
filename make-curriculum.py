Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check(a,b):
  bb = list()
  s=''
  for x in b:
    if x not in bb and x in a:
      bb.append(x)
  s=''.join(bb)
  if s==a:
    return "YES"
  else:
    return "NO"


a=input()
for _ in range(int(input())):
  print(check(a,input()))