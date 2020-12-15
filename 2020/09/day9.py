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
        index = findInvalid(numbers, 25)
        print(f'Invalid number {numbers[index]} at index {index}')

        try:
            weakness = findContiguousSum(numbers, numbers[index])
            print(f'Weakness found between indices {weakness[0]} and {weakness[1]}')

            smallest = min(numbers[weakness[0] : weakness[1] + 1])
            largest = max(numbers[weakness[0] : weakness[1] + 1])
            print(f'Smallest number: {smallest}, largest number: {largest}, sum: {smallest + largest}')
        except:
            print('No weakness found')

    except:
        print('No invalid number found')

def findInvalid(numbers, preambleLength):
    for i in range(preambleLength, len(numbers)):
        try:
            findSum(numbers[i - preambleLength : i], numbers[i])
        except:
            return i

    raise ValueError('no invalid number found')

def findSum(numbers, sum):
    for i in range(len(numbers)):
        search = sum - numbers[i]

        if search == numbers[i]:
            continue

        try:
            return (i, numbers.index(search, i + 1))
        except:
            pass
    
    raise ValueError('sum not found')

def findContiguousSum(numbers, soughtSum):
    for i in range(0, len(numbers)):
        endIndex = i
        sum = numbers[i]
        while (sum < soughtSum or endIndex == i) and endIndex < len(numbers) - 1:
            endIndex += 1
            sum += numbers[endIndex]

        if sum == soughtSum:
            return (i, endIndex)

    raise ValueError('no contiguous sum found')

if __name__ == "__main__":
    main()