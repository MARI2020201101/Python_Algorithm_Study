Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b,v=map(int,input().split())

days=0
meter=0
while True:
  meter+=a
  days+=1
  if(meter>=v): break
  meter-=b
  
print(days)