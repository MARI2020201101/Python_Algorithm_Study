Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
lists=list(map(int,input().split()))
point = 0 
result = 0
for k in lists:

  if k!=0 and k!=1:
    break
  if k==0:
    point =0
  else: 
    point +=1
  result+=point

print(result)
