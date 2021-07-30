 n=int(input())
players = list()


for i in range(n):
  a,b=map(int,input().split())
  players.append([a,b])

maxcm=0
maxcmi=0
maxkg=0
maxkgi=0

for i,p in enumerate(players):
  maxcm=max(p[0],maxcm)
  if maxcm==p[0]:
    maxcmi=i
  maxkg=max(p[1],maxkg)
  if maxkg==p[1]:
    maxkgi=i


cnt=0
for i,p in enumerate(players):
  if maxcmi==i or maxkgi==i:
    cnt+=1
  else:
    for j in range(i,n):
      f=False
      if j==maxcmi or j==maxkgi:
        continue
      elif p[0] > players[j][0] and p[1] >players[j][1]:
        f=True
    if f==True:
      cnt+=1
print(cnt)
