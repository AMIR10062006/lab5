import re
with open("row.txt","r",encoding="utf8") as file:
    regex = file.read()
pattern = re.findall("ab{2,3}",regex)
print(pattern)