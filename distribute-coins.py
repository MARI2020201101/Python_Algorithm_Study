Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
nums = [ int(input()) for i in range(n)]
print(nums)
answer = max(nums)
def dfs(i,A,B,C):
  global answer
  if i==n:
    return
  else:
    mx=max(A,B,C)
    mn=min(A,B,C)
    if((mx-mn)<answer) and A!=B and A!=C and B!=C:
      answer=mx-mn
    dfs(i+1,A+nums[i],B,C)
    dfs(i+1,A,B+nums[i],C)
    dfs(i+1,A,B,C+nums[i])



dfs(0,0,0,0)
print(answer)