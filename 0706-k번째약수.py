Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,k= map(int, input().split())

lists =[]
for i in range(1,n+1):
	if n%i==0:
		lists.append(i)

if len(lists)<k:
  print(-1)
else :
  print(lists[k-1])