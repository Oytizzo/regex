# import re

# s = "22/07/2017, 20/01/2017, 01/01/2018"

# new_s = re.sub(r'(\d{2})/(\d{2')

# s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"

# countries = s.split(",")
# print(countries)

# li = [item for item in countries if item.endswith("land")]
# print(li)

# li = re.findall(r'(\w+lands*)', s)
# print(li)

# li = re.findall(r'(\w*\s?\w+lands*)', s)
# print(li)

# compiled re
# cpat = re.compile(r'(\w*\s?\w+lands*)')
# li = cpat.findall(s)
# print(li)

# s = "Abcd 1234 - 33"
# result = re.sub(r'\d', '0', s)
# print(result)
