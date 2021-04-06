import re

with open("index.html", "r") as f:
    text = f.read()

# print(text)

# test = re.findall(r'<li>\s*(.*?)\s*<ol>', text)
# test = re.findall(r'<li>\s*(.*?)\s*<ol>.*?<li>\s*(.*?)\s*</li>.*?<li>\s*(.*?)\s*</li>', text, re.S)
# test = re.findall(r'(<li>\s*)(.*?)(\s*<ol>.*?<li>\s*)(.*?)(\s*</li>.*?<li>\s*)(.*?)(\s*</li>)', text, re.S)
# test = re.findall(r'(<li>\s*)(.*?)(\s*<ol>.*?<li>\s*)(.*?)(\s*</li>.*?<li>\s*)(.*?)(\s*</li>)', text, re.S)
# print(test)

# for item in test:
#     item = list(item)
#     print(item)

# new_s = re.sub(r'<li>\s*(.*?)\s*<ol>.*?<li>\s*(.*?)\s*</li>.*?<li>\s*(.*?)\s*</li>',r'\1 - \2, \3', text, re.S)
# new_s = re.sub(r'(<li>\s*)(.*?)(\s*<ol>.*?<li>\s*)(.*?)(\s*</li>.*?<li>\s*)(.*?)(\s*</li>)', r'\2 - \4, \6', text, re.S)
# new_s = re.search(r'(<ul>.*?<li>)', text, re.S)
# new_s = re.sub(r'(<ul>.*?<li>)\s*(.*?)\s*(<ol>.*?<li>)\s*(\w+\s*\w+)\s*(</li>\s*<li>)\s*(\w+\s*\w+)</li>',r'\g<1>' , text, re.S)
# print(new_s)

# new_s = re.search(r'(<ul>.*?<li>)\s*(.*?)\s*', text, re.S)
# print(new_s)

new_s = re.sub(r'<li>\s*(.*?)\s*<ol>\s*<li>(.*?)</li>\s*<li>(.*?)</li>\s*</ol>\s*</li>', r'\1 - \2, \3', text, re.S)
print(type(new_s))
print(new_s)
print()
new_s2 = re.findall(r'(\w+\s*-\s*\w+\s*\w+,\s*\w+\s*\w+)', new_s, re.S)
print(new_s2)
print()
for item in new_s2:
    print(item)
