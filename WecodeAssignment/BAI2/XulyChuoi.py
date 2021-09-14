s = str(input())

v = ['a','i','u','e','y','o','A','I','U','E','O','Y']

def handle(s,v) :
    news = ''
    for i in range(len(s)):
        if not s[i] in v:
            if s[i].isupper() :
                news += '.' + s[i].lower()
            else:
                news += '.' + s[i]
    return news
print(handle(s,v))