Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_soinsu(n):
  soinsu_list=[]
  i=2
  while(i<=n):
    if n%i==0:
      soinsu_list.append(i)
      n/=i
    else: i+=1

  return soinsu_list

for s in is_soinsu(int(input())): 
  print(s)