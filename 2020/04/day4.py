import sys
import re

def main():
    file = sys.stdin
    if (file.isatty()):
        filename = input('Input file name: ')
        file = open(filename)

    text = file.read()

    passports = parseBatches(text)

    counterComplete = 0
    counterValid = 0
    for passport in passports:
        if passport.hasData:
            counterComplete += 1
            if passport.isValid():
                counterValid += 1

    print(f'Complete passports: {counterComplete}')
    print(f'Valid passports: {counterValid}')

def parseBatches(text):
    rawBatches = text.split('\n\n')
    dicts = [{key: value for (key, value) in [pair.split(':') for pair in batch.split(None)]} for batch in rawBatches]
    return [Passport(dict) for dict in dicts]

class Passport:
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, fields: dict):
        for key in self.requiredFields:
            if not key in fields:
                self.hasData = False
                return

        self.hasData = True

        self.birthYear = fields['byr']
        self.issueYear = fields['iyr']
        self.expirationYear = fields['eyr']
        self.height = fields['hgt']
        self.hairColor = fields['hcl']
        self.eyeColor = fields['ecl']
        self.passportId = fields['pid']

    def isValid(self):
        if not self.hasData:
            return False

        return (
            self.__validateBirthYear() and
            self.__validateIssueYear() and
            self.__validateExpirationYear() and
            self.__validateHeight() and
            self.__validateHairColor() and
            self.__validateEyeColor() and
            self.__validatePassportId()
            )

    def __validateInteger(self, value, min, max):
        try:
            number = int(value)
            return min <= number <= max
        except:
            return False

    def __validateBirthYear(self):
        return self.__validateInteger(self.birthYear, 1920, 2002)

    def __validateIssueYear(self):
        return self.__validateInteger(self.issueYear, 2010, 2020)

    def __validateExpirationYear(self):
        return self.__validateInteger(self.expirationYear, 2020, 2030)

    def __validateHeight(self):
        if self.height.endswith('cm'):
            return self.__validateInteger(self.height[:-2], 150, 193)
        elif self.height.endswith('in'):
            return self.__validateInteger(self.height[:-2], 59, 76)

        return False

    def __validateHairColor(self):
        regex = re.compile(r'^#[0-9a-f]{6}$')
        return regex.match(self.hairColor) != None

    def __validateEyeColor(self):
        return self.eyeColor in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def __validatePassportId(self):
        return len(self.passportId) == 9 and self.__validateInteger(self.passportId, 0, 999999999)


if __name__ == '__main__':
    main()