Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
ch=[0]*(n+1)
def dfs(k):
  if k>n:
    for i in range(n+1):
      if ch[i]==1:
        print(i, end=' ')
    print()
  
  else : 
    ch[k]=0
    dfs(k+1)
    ch[k]=1
    dfs(k+1)

dfs(1)