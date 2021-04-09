import re

text = "Email your feedback here : admin@example.com admin@example py.admin@example.com book_py@example.com thank you"
result = re.findall(r'(\w+@\w+\.\w+)', text)
result2 = re.findall(r'(\w+@\w+[.]\w+)', text)
result3 = re.findall(r'([.\w]+@\w+[.]\w+)', text)

print(result3)
print(result2)
print(result)

text2 = "admin at example.com, admin At example.com, admin (at) example dot com, admin [at] example [dot] com"
text3 = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+', '@', text2, flags=re.I)
text4 = re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*\s+', '.', text3, flags=re.I)

print(text3)
print(text4)
