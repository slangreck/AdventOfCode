import sys

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name: ')
        file = open(filename)
    
    lines = file.readlines()
    file.close()

    numbers = [int(line) for line in lines]

    try:
        (indexA, indexB, indexC) = findSum(numbers, 2020, 3)
        print(f'{indexA}: {numbers[indexA]}')
        print(f'{indexB}: {numbers[indexB]}')
        print(f'{indexC}: {numbers[indexC]}')
        print(f'Product: {numbers[indexA] * numbers[indexB] * numbers[indexC]}')
    except:
        print('Could not find a solution')


def findSum(numbers, sum, partCount = 2, start = 0):
    for i in range(len(numbers)):
        search = sum - numbers[i]

        if (partCount > 2):
            try:
                return (i,) + findSum(numbers, search, partCount - 1, i + 1)
            except:
                pass
        else:
            try:
                return (i, numbers.index(search, i + 1))
            except:
                pass
    
    raise ValueError('sum not found')

if __name__ == '__main__':
    main()