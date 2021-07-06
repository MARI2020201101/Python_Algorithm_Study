Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,k=map(int,input().split())
lists = list(map(int,input().split()))
sets = set()

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      sets.add(lists[i]+lists[j]+lists[k])


kth = list(sets)
kth.sort(reverse=True)
print(kth[k-1])