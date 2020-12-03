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

    print(f'Number of valid passwords for sledding policy: {len([True for (policy, password) in policiesAndPasswords if checkPasswordSledding(policy, password)])}')
    print(f'Number of valid passwords for toboggan policy: {len([True for (policy, password) in policiesAndPasswords if checkPasswordToboggan(policy, password)])}')

def parsePasswordPolicy(input):
    match = PASSWORD_REGEX.match(input)
    if not match:
        return None

    return (PasswordPolicy(match.group(3), int(match.group(1)), int(match.group(2))), match.group(4))

def checkPasswordSledding(policy, password):
    count = password.count(policy.requiredChar)
    return count >= policy.firstNumber and count <= policy.secondNumber

def checkPasswordToboggan(policy, password):
    firstChar = password[policy.firstNumber - 1]
    secondChar = password[policy.secondNumber - 1]

    return (firstChar == policy.requiredChar) ^ (secondChar == policy.requiredChar)

class PasswordPolicy(NamedTuple):
    requiredChar: str
    firstNumber: int
    secondNumber: int

if __name__ == '__main__':
    main()