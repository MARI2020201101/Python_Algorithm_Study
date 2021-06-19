Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(S, C):

   count=S.count(',')
   n=0
   for _ in range(count+1):
      
      email=''
      first=''
      middle=''
      last=''
      print('SSS>>',S)
      comma=S.index(', ')
      print(comma)
      target=S[n:comma]
      s = target.lower()
      S=S[comma+1:]
      print(S)
      fullname=s.split(' ')
      if len(fullname)==3:
         first=fullname[0]
         middle=fullname[1]
         last=fullname[2]
         n+=2
      else:
         first=fullname[0]
         last=fullname[1]
         n+=1
      if last.find('-')>0:
         last.remove('-')
         n+=1
      email=first+middle+last
      n+=len(email)
      names = {}
      if(email in names):
         names[email]+=1
         email=email+ str(names[email])
      else:
         names[email]=1
      c=C.lower()
      email='<'+email+'@'+c+'.com>'
      print(email)
      