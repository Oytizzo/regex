import re

s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"

# countries = s.split(",")
# print(countries)

# li = [item for item in countries if item.endswith("land")]
# print(li)

li = re.findall(r'(\w+lands*)', s)
print(li)
