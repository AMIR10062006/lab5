import re
def snaketocamel(sc):
    cc = re.sub(r'_(\w)',lambda x: x.group(1).upper(),sc)
    return cc
if __name__ == "__main__":
    string = str(input("write some string: "))
    print(snaketocamel(string))