Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> h,m=map(int,input().split())
if m>45: print(h,m-45)
else: print(((h-1)%24),((m-45)%60))
