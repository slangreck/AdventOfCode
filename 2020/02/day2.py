import sys
import re
from typing import NamedTuple

PASSWORD_REGEX = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)');

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name: ')
        file = open(filename)
    
    lines = file.readlines()
    file.close()

    policiesAndPasswords = [parsePasswordPolicy(line) for line in lines]

    print(len([True for (policy, password) in policiesAndPasswords if checkPassword(policy, password)]))

def parsePasswordPolicy(input):
    match = PASSWORD_REGEX.match(input)
    if not match:
        return None

    return (PasswordPolicy(match.group(3), int(match.group(1)), int(match.group(2))), match.group(4))

def checkPassword(policy, password):
    count = password.count(policy.requiredChar)
    return count >= policy.minOccurances and count <= policy.maxOccurances

class PasswordPolicy(NamedTuple):
    requiredChar: str
    minOccurances: int
    maxOccurances: int

if __name__ == '__main__':
    main()