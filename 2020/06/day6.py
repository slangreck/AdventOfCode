import sys

def main():
    file = sys.stdin
    if (file.isatty()):
        filename = input('Input file name: ')
        file = open(filename)

    text = file.read()

    groups = text.split('\n\n')

    uniqueAnswers = [set(''.join(group.split())) for group in groups]

    sum = 0
    for answer in uniqueAnswers:
        sum += len(answer)

    print(sum)

if __name__ == "__main__":
    main()