Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
musics=list(map(int,input().split()))
start=0
end=sum(musics)
answer=sum(musics)
while(start<=end):
  mid=(start+end)//2
  cnt=check(musics,mid)
  if cnt<=m:  
    answer=min(answer,mid)
    print(answer)
    end=mid-1
  elif cnt>m:
    start=mid+1

print(answer)
