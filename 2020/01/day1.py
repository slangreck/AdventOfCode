import sys

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name: ')
        file = open(filename)
    
    lines = file.readlines()
    file.close()

    numbers = [int(line) for line in lines]

    sum = 0
    partCount = 0

    if len(sys.argv) == 3:
        sum = int(sys.argv[1])
        partCount = int(sys.argv[2])
    else:
        sum = int(input('Sum to search: '))
        partCount = int(input('Number of parts of the sum: '))

    try:
        indices = findSum(numbers, sum, partCount)
        product = 1
        for index in indices:
            print(f'{index}: {numbers[index]}')
            product *= numbers[index]
        print(f'Product: {product}')
    except:
        print('Could not find a solution')


def findSum(numbers, sum, partCount = 2, start = 0):
    if partCount < 2:
        raise ValueError('partCount must not be smaller than 2')

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