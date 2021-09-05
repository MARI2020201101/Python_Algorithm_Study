Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def DFS(x):
  if x>7:
    return
  else:
    DFS(x*2)
    DFS(x*2+1)
    print(x,end=' ')

DFS(1)