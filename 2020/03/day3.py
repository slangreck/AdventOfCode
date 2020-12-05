import sys

def main():
	file = sys.stdin
	if file.isatty():
		filename = input('Input file name: ')
		file = open(filename)

	lines = file.readlines()
	file.close()

	map = [[char == '#' for char in line.strip()] for line in lines]

	print(f'Crashed into {goSledding(map)} trees')

def goSledding(map):
	counter = 0
	horizontal = 0

	for line in map:
		if line[horizontal]:
			counter = counter + 1
		horizontal = (horizontal + 3) % len(line)

	return counter

if __name__ == '__main__':
	main()
