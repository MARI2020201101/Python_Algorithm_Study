Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
1/1, 1/2, 2/1, 3/1, 2/2, 1/3, 1/4, 2/3, 3/2, 4/1,...

1 / 1,2 / 3,2,1 / 1,2,3,4
1 / 2,1 / 1,2,3 / 4,3,2,1
1개 2개 3개 4개
index = sum([i for i in range(1,n+1)])
1 3 6 10 15 ....
f(n)+=n
f.index(n)
nums =[]
nums[0] = 0
nums[1] = 1
nums[2] = 12
nums[3] = 123
'''
#n>1
idx_list=[]
idx=0
for i in range(1,n+1):
  idx+=i
  idx_list.append(idx)


def nums(n):
  if n==0:
    return ''
  if n==1:
    return '1'
  return nums(n-1)+str(n)

def mkfraction(m):

