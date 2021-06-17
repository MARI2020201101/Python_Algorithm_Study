Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m = int(input())
for mm in range(m):
  n,word=input().split()
  new_word=""
  for w in word:
    for i in range(int(n)):
      new_word+=w
  print(new_word)
  