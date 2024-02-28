import re
with open("row.txt","r",encoding="utf8") as file:
    regex = file.read()
pattern = re.findall("[A-Z]{1}[a-z]+",regex)
print(pattern)