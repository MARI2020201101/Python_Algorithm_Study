Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fac(n):
  if n==0 or n==1:
    return 1
  return n*fac(n-1)

N = int(input()) 
print(fac(N))