import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
print(response.ok)
text = response.text
# print(len(text))

result = re.findall(r'<div class="side_categories">(.*?)</div>', text, re.M | re.DOTALL)
# print(len(result))
s = result[0]
# print(s)

category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M | re.DOTALL)
result = re.findall(category_pat, s)
print(len(result))
# print(result[0])

for item in result:
    print(item)
