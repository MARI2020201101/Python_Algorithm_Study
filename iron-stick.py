Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
aaa=list()
for aa in a:
  aaa.append(aa)
stack=[]
lcount = 0
rcount = 0
result = 0
for n in aaa:
  if n=='(':
    lcount+=1
  else:
    rcount+=1
    result+=lcount-rcount
    lcount=lcount-rcount
    rcount=0
print(result)
