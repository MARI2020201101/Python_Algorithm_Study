Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c,n=map(int,input().split())
dogs=list()
for i in range(n):
  dogs.append(int(input()))

def dfs(idx,mx):
  if idx==n and mx<c:
    print(mx)

  else: 
    if mx<c:
      dfs(idx+1,mx)
      dfs(idx+1,mx+dogs[idx])

dfs(0,0)