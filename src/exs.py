import re

with open("index.html", "r") as f:
    text = f.read()

# print(type(text))

# worked 1
new_s = re.sub(r'<li>\s*(.*?)\s*<ol>\s*<li>(.*?)</li>\s*<li>(.*?)</li>\s*</ol>\s*</li>', r'\1 - \2, \3', text, re.S)
print(type(new_s))
print(new_s)
print()
new_s2 = re.findall(r'(\w+\s*-\s*\w+\s*\w+,\s*\w+\s*\w+)', new_s, re.S)
print(new_s2)
print()
for item in new_s2:
    print(item)

print()
print()
print()

# worked 2
test = re.findall(r'<li>\s*(.*?)\s*<ol>.*?<li>\s*(.*?)\s*</li>.*?<li>\s*(.*?)\s*</li>', text, re.S)
print(test)

for item in test:
    s = item[0] + ' - ' + item[1] + ', ' + item[2]
    print(s)
