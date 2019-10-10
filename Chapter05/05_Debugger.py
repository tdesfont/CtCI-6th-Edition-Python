import sys

def debugger(n):
	return ((n & (n-1)) == 0)

if __name__ == "__main__":
	print(debugger(int(sys.argv[1])))