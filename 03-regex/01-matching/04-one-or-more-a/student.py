import re

def equals_abc(string):
    return re.fullmatch('a+', string)