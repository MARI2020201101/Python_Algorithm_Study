Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
square=[]
for i in range(n):
  square.append(list(map(int,input().split())))
maxr=0
maxc=0
maxd=0
for i in range(len(square)):
  temp=0
  temp2=0
  for j in range(len(square)):
    temp+=square[i][j]
    temp2+=square[j][i]
  maxr=max(temp,maxr)
  maxc=max(temp2,maxr)

temp3=0
temp4=0
for i in range(len(square)):
  temp3+=square[i][i]
  temp4+=square[-(i+1)][-(i+1)]
maxd=max(temp3,temp4)

answer=0
if maxr>maxc and maxr>maxd:
  answer=maxr
elif maxc>maxr and maxc>maxd:
  answer=maxc
else:
  answer=maxd

print(answer)