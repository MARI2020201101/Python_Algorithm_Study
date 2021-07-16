Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import combinations
def insert(stack,n,m):
  for k in range(n,m):
    stack.append(k)
  return stack


N=int(input())
lists = list()
for i in range(1,N+1):
  lists.append(i)
when = list()  
for i in range(1,N+1):
  for j in combinations(lists, i):
    when.append(j)

stack=list()
for n in when:
  prev=0
  for num in n:
    if prev==0:
      prev=num
    stack=insert(stack,prev,num+1)
    while(len(stack)!=0) : 
      
      print(stack.pop(), end=' ')
    prev=num+1
''''
  if n[-1]!=N:
    for i in range(N,n[-1],-1):
      print(i, end=' ')



  '''

    