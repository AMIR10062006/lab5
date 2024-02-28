import re
def space(string):
    spaced = re.sub(r'([a-z])([A-Z])',r'\1 \2',string)
    return spaced
if __name__ == "__main__":
    string = str(input())
    print(space(string))