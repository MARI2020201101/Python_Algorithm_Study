Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
tmp=list()
def dfs(i,tmp):
  if(i==m):
    print(tmp,end=" ")
  else: 
    dfs(i+1,tmp.append(i))
    dfs(i+1,tmp)

dfs(0,tmp)
