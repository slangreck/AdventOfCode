import sys

def main():
    file = sys.stdin
    if (file.isatty()):
        filename = input('Input file name: ')
        file = open(filename)

    text = file.read()

    groups = text.split('\n\n')

    answerLists = [[set(answer.strip()) for answer in group.split()] for group in groups]

    anySum = 0
    everySum = 0
    for answerList in answerLists:
        if len(answerList) > 0:
            anySum += len(set.union(*answerList))
            everySum += len(set.intersection(*answerList))

    print(f'Sum of questions any person answered yes: {anySum}')
    print(f'Sum of questions every person answered yes: {everySum}')

if __name__ == "__main__":
    main()