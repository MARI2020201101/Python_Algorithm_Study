Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
scores =list(map(int,input().split()))
minlen = 100
minscore = list()
avgscore = int(round(sum(scores)/n,0))
#print(avgscore)

for i in range(n):
  minlen = min(abs(avgscore-scores[i]), minlen)
for i in range(n):
  if minlen==abs(avgscore-scores[i]):
    minscore.append((scores[i], i+1))

minscore.sort(reverse=True)
#print(minscore)

minscores=list()
minvalue = minscore[0][0]
for i in range(len(minscore)):
  if minscore[i][0]==minvalue:
    minscores.append(minscore[i][1])

#print(minscores)
print(avgscore, minscores[-1])