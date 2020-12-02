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
        (indexA, indexB) = findSum(numbers, 2020)
        print(f'{indexA}: {numbers[indexA]}')
        print(f'{indexB}: {numbers[indexB]}')
        print(f'Product: {numbers[indexA] * numbers[indexB]}')
    except:
        print('Could not find a solution')


def findSum(numbers, sum):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if i != j and numbers[i] + numbers[j] == sum:
                return (i, j)
    
    raise ValueError('sum not found')

if __name__ == '__main__':
    main()