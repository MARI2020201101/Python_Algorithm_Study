
def issame(strr):
  if strr == strr[::-1]:
    return "YES"
  else:
    return "NO"


n = int(input())
for i in range(1, n+1):
  strr=input()
  strr=strr.upper()
  print("#"+str(i) +" "+ issame(strr))
