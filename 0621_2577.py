Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A=int(input())
B=int(input())
C=int(input())

multiple = A*B*C
list =[0]*10
multiple = str(multiple)
for i in range(len(multiple)):
  list[int(multiple[i])]+=1
for n in range(len(list)):
  print(list[n])