Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_leap(year):
    leap = False
    if year%4==0:
        leap = True
        if year%100==0:
            leap = False
        if year%400==0:
            leap = True
    
    
    return leap

year = int(input())
print(is_leap(year))