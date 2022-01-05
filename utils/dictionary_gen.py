#!/usr/bin/python3

def dict_gen():
	x0 = 116
	y0 = 986
	xDelta = x0 - 257
	yDelta = y0 -1106

	xnum = 7
	ynum = 10
	xCurr= x0
	yCurr = y0

	counter = 1

	coordDict = {}

	for i in range(0, ynum):
		for j in range (0, xnum):
			print(f"Coordinates of number {counter}")
			print( xCurr, yCurr)
			coordDict[counter] = (xCurr, yCurr)
			xCurr = xCurr - xDelta
			counter += 1
		yCurr = yCurr - yDelta
		xCurr = x0
		
	return coordDict

if __name__ == "__main__":
	dict_gen()
	