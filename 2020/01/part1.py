import sys

def main():
    if sys.stdin.isatty():
        print('Please pipe input into stdin')
        exit()
    
    lines = sys.stdin.readlines()
    numbers = [int(line) for line in lines]

    try:
        (indexA, indexB) = findSum(numbers, 2020)
        print('{0}: {1}'.format(indexA, numbers[indexA]))
        print('{0}: {1}'.format(indexB, numbers[indexB]))
        print('{0}: {1}'.format('Product', numbers[indexA] * numbers[indexB]))
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