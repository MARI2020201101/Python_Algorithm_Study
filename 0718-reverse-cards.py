Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def change(cards,n,m):
  a = cards[:n]
  b = cards[m:n-1:-1]
  c = cards[m+1:]
  cards = a+b+c
  return cards



cards=[i for i in range(21)]

for i in range(10):
  n,m=map(int,input().split())
  cards = change(cards,n,m)
cards.remove(0)
print(*cards)
