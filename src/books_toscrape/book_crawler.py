import sys
import requests
import re
import csv
import logging
from html import unescape

def get_category_list(content):
    """get_category_list() takes the content of the home page and returns
    a list of category and their urls"""

    return category_list_pat.findall(content)

def get_page_content(url):
    """get_page_content() takes an url and returns the content of that page"""

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logging.error(e)
    
    if response.ok:
        return response.text
    
    logging.error("Can not get content from URL: " + url)

    return ""


def crawl_website():
    """Main function that does the crawling"""

    url = "http://books.toscrape.com/"

    content = get_page_content(url)
    if content == "":
        logging.critical("Got empty content from " + url)
        sys.exit(1)
    
    category_list = get_category_list(content)
    print(len(category_list))
    for category in category_list:
        print(category)

if __name__ == "__main__":
    # Compiler for regex
    category_list_pat = re.compile(
        r'<li>\s*<a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*?</a>', 
        re.M | re.DOTALL)

    # logging
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', 
    filename="bookstore_crawler.log", level=logging.DEBUG)

    # csv

    # crawl
    crawl_website()
    # print done!