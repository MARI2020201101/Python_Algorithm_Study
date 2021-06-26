Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
    N = int(input())
    lists = []
    for i in range(N):
        commands=list(input().split())
        command = commands[0] 
        if command =='insert':
            lists.insert(int(commands[1]),int(commands[2]))
        if command =='print':
            print(lists)
        if command =='remove':
            lists.remove(int(commands[1]))
        if command =='append':
            lists.append(int(commands[1]))
        if command =='sort':
            lists.sort()
        if command =='pop':
            lists.pop()
        if command =='reverse':
            lists.reverse()
        