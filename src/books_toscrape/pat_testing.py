import requests
import re

url = "http://books.toscrape.com/"                                                  # main url
print(url)

response = requests.get(url)
content = response.text                                                             # content
# print(len(content))
category_list_pat = re.compile(
    r'<li>\s*<a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*?</a>', 
    re.M | re.DOTALL)                                                               # category_list_pat
category_list = category_list_pat.findall(content)                                  # category list
print(len(category_list))                                                           # category len = 50
# for category in category_list:
#     print(category)

# category starts here -----------------------------------------------------------------
category1 = category_list[0]                                                        # category 1

category1_url = category1[0]
category1_name = category1[1]

# print("Name: ", category1_name)
# print("URL: ",  category1_url)

category1_url = url + category1_url                                                 # category url
print(category1_url)

response = requests.get(category1_url)
content = response.text
content = content.replace("\n", "")                                                 # content
# print(content)
book_list_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')                   # book_list_pat
book_list = book_list_pat.findall(content)                                          # book list
print(len(book_list))                                                               # book list = 11
# for book in book_list:
#     print(book)

# book starts here -----------------------------------------------------------------
# book1 = 

# next page starts here ------------------------------------------------------------
next_page_pat = re.compile(r'<li class="next"><a href="(.*?)">next</a></li>')       # next_page_pat
next_page = next_page_pat.findall(content)                                          # next_page
print(next_page)
print(len(next_page))
# if len(next_page) == 0:
#     print(next_page)
# i = category1_url.rfind("/")
# next_page_url = category1_url[0:i+1] + next_page[0]
# print(next_page_url)
