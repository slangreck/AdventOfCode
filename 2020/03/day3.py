import sys

def main():
	file = sys.stdin
	if file.isatty():
		filename = input('Input file name: ')
		file = open(filename)

	lines = file.readlines()
	file.close()

	map = [[char == '#' for char in line.strip()] for line in lines]

	runs = [
		(1, 1),
		(3, 1),
		(5, 1),
		(7, 1),
		(1, 2)
	]

	product = 1
	for run in runs:
		crashes = goSledding(map, run[0], run[1])
		print(f'Right {run[0]}, down {run[1]}: {crashes}')
		product = product * crashes

	print(f'Product: {product}')

def goSledding(map, stepHorizontal, stepVertical):
	counter = 0
	horizontal = 0

	for line in map[::stepVertical]:
		if line[horizontal]:
			counter = counter + 1
		horizontal = (horizontal + stepHorizontal) % len(line)

	return counter

if __name__ == '__main__':
	main()
