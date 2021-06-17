Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isPrime(n):
  count = 0
  result = 0
  for i in range(2,n):
    if n%i==0: 
      result+=1
  if result==0:
    count+=1
  return count

cnt=0
start = int(input())
end = int(input())
prime_list = []
for n in range(start, end+1): 
  if isPrime(n)==1:
    prime_list.append(n)

if len(prime_list)<1: 
  print(-1)
else:
  sum_prime = sum(prime_list)
  min_prime = min(prime_list)

  print(sum_prime)
  print(min_prime)