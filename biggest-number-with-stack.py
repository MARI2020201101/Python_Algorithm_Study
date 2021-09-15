Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
n=list(map(str,str(n)))
stack=[]
for x in n:
  while stack and m>0 and stack[-1]<x:
    stack.pop()
    m-=1
  stack.append(x)
if m!=0:
  stack=stack[:-m]

stack=''.join(stack)
print(stack)