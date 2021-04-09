# Web scrapping from the bookshop website
import requests
import re

# -------------------------------1-----------------------------
# url = "http://books.toscrape.com/index.html"
# response = requests.get(url)
# print(response.ok)
# text = response.text
# # print(len(text))

# result = re.findall(r'<div class="side_categories">(.*?)</div>', text, re.M | re.DOTALL)
# # print(len(result))
# s = result[0]
# # print(s)

# category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M | re.DOTALL)
# result = re.findall(category_pat, s)
# print(len(result))
# # print(result[0])

# for item in result:
#     print(item)

# --------------------------------2--------------------------
# url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
# response = requests.get(url)
# text = response.text
# text = text.replace("\n", " ")
# book_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')

# books = re.findall(book_pat, text)
# # print(len(books))

# # for item in books:
# #     print(item)

# next_page = re.findall(r'<li class="next"><a href="(.*?)">next</a></li>', text)
# # print(next_page)
# i = url.rfind("/")
# # print(i)
# # print(type(i))
# # print(url[:i+1])
# url = url[:i+1] + next_page[0]
# # print(url)

# ---------------------------------3----------------------------------
# url = "http://books.toscrape.com/catalogue/the-exiled_247/index.html"
# response = requests.get(url)
# text = response.text
# text = text.replace("\n", " ")
# book_image_pat = re.compile(r'<div class="item active">\s*<img src="(.*?)" alt')
# book_image = re.findall(book_image_pat, text)
# print(book_image[0])
# print("")

# book_description_pat = re.compile(r'<div id="product_description" class="sub-header">.*?<p>(.*?)</p>')
# book_description = re.findall(book_description_pat, text)
# print(book_description[0])
# print("")

# upc_pat = re.compile(r'<th>UPC</th>\s*<td>(.*?)</td>')
# upc = re.findall(upc_pat, text)
# print(upc[0])
# print("")

# price_pat = re.compile(r'<th>Price\s*\(incl.\s*tax\)</th>\s*<td>(.*?)</td>')
# price = re.findall(price_pat, text)
# print(price[0])

# availability_pat = re.compile(r'<th>Availability</th>\s*\<td>(.*?)</td>')
# availability = re.findall(availability_pat, text)
# print(availability[0])
