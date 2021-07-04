Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
mid = n//2
str = '.|.'
wstr = 'WELCOME'
i=1
for i in range(mid):
    print(str.center(m,'-'))
    str += '.|..|.'
print(wstr.center(m,'-'))


str = '.|.'
ii = 2*mid-1

for i in range(n-mid-1):
    print((str*(ii)).center(m,'-'))
    ii-=2