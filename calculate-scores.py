Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(scores):
    n = len(scores)
    def solution(scores):
    n = len(scores)
    avgs = list()
    for i in range(n):
      avg=list()
      for j in range(n):
        avg.append(scores[j][i])
      avgs.append(isM(avg,scores,n,i))
    answer=evaluate(avgs)
    answer=''.join(answer)
    return answer
def isM(avg,scores,n,i):
  sortedavg = sorted(avg)
  if scores[i][i]==sortedavg[0] and scores[i][i]!=sortedavg[1]:
    sortedavg.pop(0)
  elif scores[i][i]==sortedavg[n-1] and scores[i][i]!=sortedavg[n-2]:
    sortedavg.pop()
  return calculate(sortedavg)
  
def calculate(sortedavg):
  return sum(sortedavg)/len(sortedavg)

def evaluate(avgs):
  grade = list()
  for i in range(len(avgs)):
    if avgs[i]>=90:
      grade.append('A')
    elif avgs[i]>=80:
      grade.append('B')
    elif avgs[i]>=70:
      grade.append('C')
    elif avgs[i]>=50:
      grade.append('D')
    else:
      grade.append('F')
  return grade  