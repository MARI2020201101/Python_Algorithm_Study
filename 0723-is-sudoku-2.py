Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=[list(map(int,input().split()))for i in range(9)]

ch1=[0]*10
ch2=[0]*10
ch4=True
for i in range(9):
  for j in range(9):
    ch1[s[i][j]]=1
    ch2[s[j][i]]=1
if sum(ch1[1:])==9 and sum(ch2[1:])==9:
  
  for p in range(3):
    for q in range(3):
      ch3=[0]*10
      for k in range(3):
        for l in range(3):
          ch3[s[k+(p*3)][l+(q*3)]]=1
      if sum(ch3[1:])==9:
        continue
      else:
        ch4=False    
        break
  if ch4==True:
    print("YES")   
  else:
    print("NO")           
else: 
  print("NO")
      