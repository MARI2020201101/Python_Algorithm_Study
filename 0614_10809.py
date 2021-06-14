Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> alpha=input()
alpabet_list=[0]*26
for a in alpha:
  alpabet_list[ord(a)-97]=alpha.find(a)
for i in range(len(alpabet_list)):
  if alpabet_list[i]==0:
    alpabet_list[i]=-1
 # alpabet_list[alpha.find(alpha[0])]=0
print(*alpabet_list)
