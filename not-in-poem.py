Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
words=set([input(i) for i in range(n)])
poem=set([input(i) for i in range(1,n)])

for w in words:
  if w not in poem:
    print(w)
    break