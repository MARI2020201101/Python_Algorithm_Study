Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> S = input()
target = input()
count = 0
for i in range(len(S)-len(target)+1):
    
    search = S[i:i+len(target)]
    tup = (i,i+len(target)-1)
    if search==target:
        print(tup)
        count +=1
if count==0:
    print((-1,-1))