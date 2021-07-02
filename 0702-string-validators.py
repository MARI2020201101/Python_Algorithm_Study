Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
    S = input()
    flags = [False]*5
    for s in S:
        flag = False    
        if s.isalnum():
            flag = True
            flags[0] = flag
        if s.isalpha():
            flag = True
            flags[1] = flag
        if s.isdigit():
            flag = True
            flags[2] = flag
        if s.islower():
            flag = True
            flags[3] = flag
        if s.isupper():
            flag = True
            flags[4] = flag

    for f in flags:
        print(f)