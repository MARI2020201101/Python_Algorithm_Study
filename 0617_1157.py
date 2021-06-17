Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string =input().upper()
count =[0]*26

for s in string:
  count[ord(s)-ord('A')]+=1
#print(*count)
count_sorted = sorted(count)
#print(*count)
if(count_sorted[len(count_sorted)-1]==count_sorted[len(count_sorted)-2]):
  print('?')

#print(max(count))
else :
  print(chr(count.index(max(count))+ord('A')))