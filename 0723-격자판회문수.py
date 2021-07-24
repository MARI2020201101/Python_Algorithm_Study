Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> square = [list(input().split()) for _ in range(7)]
cnt=0
for i in range(7):
  s=0
  e=5
  a=square[i]
  while(s<3):
    strr = "".join(a[s:e])
    if strr==strr[::-1]:
      cnt+=1
    s+=1
    e+=1


for i in range(7):
  b=list()
  s=0
  e=5
  for j in range(7):
    b.append(square[j][i])
  while(s<3):
    strrr = "".join(b[s:e])
    if strrr==strrr[::-1]:
      cnt+=1
    s+=1
    e+=1

print(cnt)