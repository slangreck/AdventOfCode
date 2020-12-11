import sys

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name:')
        file = open(filename)
    
    lines = file.readlines()
    file.close()

    instructions = [Instruction(code) for code in lines]

    print(f'Value of acc when loop occurs: {runProgramUntilLoop(instructions)}')

def runProgramUntilLoop(instructions):
    ip = 0
    acc = 0

    instruction = instructions[ip]
    while not instruction.executed:
        if instruction.command == 'acc':
            acc += instruction.parameter
            ip += 1
        elif instruction.command == 'jmp':
            ip += instruction.parameter
        else:
            ip += 1
        
        instruction.executed = True
        instruction = instructions[ip]

    return acc

class Instruction:
    def __init__(self, code):
        (self.command, parameter) = code.strip().split()
        self.parameter = int(parameter)
        self.executed = False

if __name__ == "__main__":
    main()