Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
lists=list(map(int,input().split()))
lt=0
rt=n-1
last=0
answer=""
tmp=list()
while lt<=rt:
  if last<lists[lt]:
    tmp.append((lists[lt],'L'))
  if last<lists[rt]:
    tmp.append((lists[rt],'R'))
  if len(tmp)==0:
    break
  tmp.sort()
  answer+=tmp[0][1]
  if tmp[0][0]==lists[lt]:
    last=lists[lt]
  if tmp[0][0]==lists[rt]:
    last=lists[rt]
  tmp.clear()

print(len(answer))
print(answer)
