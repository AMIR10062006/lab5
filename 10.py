import re
def cameltosnake(camel):
    snake = re.sub(r'([a-z0-9])([A-Z])',r'\1_\2',camel).lower()
    return snake
if __name__ =="__main__":
    camel = str(input("input camel string: "))
    print(cameltosnake(camel))
