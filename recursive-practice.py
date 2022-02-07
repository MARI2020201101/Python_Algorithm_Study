Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
def dfs(idx,answer):
  if idx==m:
    print(*answer)
  else:
    dfs(idx+1,answer.append(idx+1))
    dfs(idx,answer)

answer=list()
dfs(0,answer)
