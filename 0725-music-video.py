Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check(musics,cnt,minn):
  sums=0
  start=0
  while(sums<minn):
    for i in range(start,len(musics)):
      sums+=musics[i]
      start=i+1
    cnt+=1
    sums=0
      
  return cnt

n,m=map(int,input().split())
musics=list(map(int,input().split()))
minn=max(musics)
cnt=0

while(True):
  cnt=check(musics,cnt,minn)
  if cnt==m:
    break
  else:
    cnt=0
    minn+=1
print(cnt)
  