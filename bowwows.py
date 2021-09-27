Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c,n=map(int,input().split())
kg=list(map(int, input().split()))

def dfs(idx,k,mx):
  if idx>n:
    if mx<k<c:
      mx=k
      print(mx)
      return
    else:
      return
  else: 
    dfs(idx+1,k+kg[idx],mx)
    dfs(idx+1,k,mx)


dfs(0,0,0)