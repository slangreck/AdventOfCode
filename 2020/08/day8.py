import sys

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name: ')
        file = open(filename)
    
    lines = file.readlines()
    file.close()

    instructions = [Instruction(code) for code in lines]

    print(f'Value of acc when loop occurs: {runProgramUntilLoop(instructions)[0]}')

    for instruction in instructions:
        if instruction.command == 'jmp':
            instruction.command = 'nop'
            (acc, terminated) = runProgramUntilLoop(instructions)

            if terminated:
                print(f'Value of acc after termination: {acc}')
                return
            
            instruction.command = 'jmp'
        elif instruction.command == 'nop':
            instruction.command = 'jmp'
            (acc, terminated) = runProgramUntilLoop(instructions)

            if terminated:
                print(f'Value of acc after termination: {acc}')
                return
            
            instruction.command = 'nop'

def runProgramUntilLoop(instructions):
    ip = 0
    acc = 0

    for instruction in instructions:
        instruction.executed = False

    while ip < len(instructions):
        instruction = instructions[ip]
        if instruction.executed:
            return (acc, False)

        if instruction.command == 'acc':
            acc += instruction.parameter
            ip += 1
        elif instruction.command == 'jmp':
            ip += instruction.parameter
        else:
            ip += 1
        
        instruction.executed = True

    return (acc, True)

class Instruction:
    def __init__(self, code):
        (self.command, parameter) = code.strip().split()
        self.parameter = int(parameter)
        self.executed = False

if __name__ == "__main__":
    main()