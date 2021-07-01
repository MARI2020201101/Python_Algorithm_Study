Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import Counter

x= int(input())
shoe = list(map(int,input().split()))
shoe_list = Counter(shoe)
income = 0
for _ in range(int(input())):
   size, money = map(int,input().split())
   if size in shoe_list and shoe_list[size] > 0:
    income += money
    shoe_list[size]-=1
print(income)