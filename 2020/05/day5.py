import sys
import math

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name: ')
        file = open(filename)

    lines = file.readlines()
    boardingPasses = [BoardingPass(line) for line in lines]
    boardingPasses.sort(key = lambda boardingPass: boardingPass.seatID)
    
    print(f'Highest seat ID is {boardingPasses[-1]. seatID}')

    seatIDs = [boardingPass.seatID for boardingPass in boardingPasses]

    for seatID in range(1, 127 * 8 + 7 -1):
        if seatID not in seatIDs and (seatID - 1) in seatIDs and (seatID + 1) in seatIDs:
            print(f'There is a free seat with ID {seatID}')

class BoardingPass:
    def __init__(self, seatcode):
        seatcode = seatcode.strip()
        self.seatcode = seatcode
        self.row = self.__decodeRow(seatcode[:-3])
        self.column = self.__decodeColumn(seatcode[-3:])
        self.seatID = self.row * 8 + self.column

    def __decodeRow(self, rowcode):
        return self.__decodeBSP(list(rowcode), 0, 127, 'F', 'B')

    def __decodeColumn(self, columncode):
        return self.__decodeBSP(list(columncode), 0, 7, 'L', 'R')

    def __decodeBSP(self, code, start, end, tokenLower, tokenUpper):
        if len(code) == 0 or start >= end:
            return start

        token = code.pop(0)
        if token == tokenLower:
            end -= math.ceil((end - start) / 2)
        elif token == tokenUpper:
            start += math.ceil((end - start) / 2)

        return self.__decodeBSP(code, start, end, tokenLower, tokenUpper)

if __name__ == "__main__":
    main()