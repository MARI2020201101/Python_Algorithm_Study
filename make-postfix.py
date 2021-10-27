Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input()
stack=[]
answer=''
for x in a:
  if x.isdecimal():
    answer+=x
  elif x=='*'or x=='/':
    while stack and (stack[-1]=='*'or stack[-1]=='/'):
      answer+=stack.pop()
    stack.append(x)
  elif x=='+' or x=='-':
    while stack and (stack[-1]=='('):
      answer+=stack.pop()
    stack.append(x)
  elif x=='(':
    while stack and (stack[-1]=='*'or stack[-1]=='/'):
      answer+=stack.pop()
while stack:
  answer+=stack.pop()
print(answer)
