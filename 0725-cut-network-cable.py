Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k,n=map(int,input().split())
lines = [int(input()) for _ in range(k)]
linesum=sum(lines)
line=linesum//n

while(True):
  nn=0
  for l in lines:
    nn+=l//line
  if nn==n:
    break
  else:
    line-=1

print(line)