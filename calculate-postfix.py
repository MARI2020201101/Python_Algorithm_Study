Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
stack=[]
for x in a:
  if x.isdecimal():   
    stack.append(int(x))
  else:
    xx=str(stack[-2]) + x + str(stack[-1])
    stack.pop()
    stack.pop()
    xx=eval(xx)
    stack.append(xx)

print(*stack)