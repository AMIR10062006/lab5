import re
with open("row.txt","r",encoding="utf8") as file:
    regex = file.read()
pattern = re.findall("a.+b$",regex)
print(pattern)