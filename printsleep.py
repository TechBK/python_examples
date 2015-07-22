import asyncio

def main():
	result = yield from asyncio.sleep(1.0)
	print(result)	

if __name__ == "__main__":
	main()
