import re
def splitter(string):
    splittedlist = re.findall('[A-Z][^A-Z]*',string)
    res = ' '.join(splittedlist)
    return res
if __name__ == "__main__":
    string = str(input())
    print(splitter(string))
