Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def pivo(n):
  if n==0:
    return 0
  if n==1:
    return 1
  return pivo(n-1)+pivo(n-2)

print(pivo(int(input())))