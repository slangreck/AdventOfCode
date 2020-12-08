import sys

def main():
    file = sys.stdin
    if (file.isatty()):
        filename = input('Input file name: ')
        file = open(filename)

    text = file.read()

    passports = parseBatches(text)

    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    counter = 0
    for passport in passports:
        if validatePassport(passport, requiredFields):
            counter += 1

    print(f'Valid passports: {counter}')

def parseBatches(text):
    rawBatches = text.split('\n\n')
    return [{key: value for (key, value) in [pair.split(':') for pair in batch.split(None)]} for batch in rawBatches]

def validatePassport(passport: dict, requiredFields: list):
    for key in requiredFields:
        if not key in passport:
            return False

    return True

if __name__ == '__main__':
    main()