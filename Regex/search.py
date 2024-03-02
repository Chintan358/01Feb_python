import re


str = "sun rises in east"

# a = re.search('in',str)
# r =a.span()
# print(r)

# regex =  re.compile('in')
# str = regex.sub("abcd",str)
# print(str)

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
k = re.match(pattern, "abc@gmail.com") 
print(k)





for i in re.finditer('in',str):
    result = i.span()
    print(result)