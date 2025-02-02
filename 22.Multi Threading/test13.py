import time
from multiprocessing import Pool

def sum_square(number):
	sum = 0
	for i in range(number):
		sum += i*1
	return sum

def sum_square_with_mp(numbers):
	start_time = time.time()
	p = Pool(8)
	result = p.map(sum_square,numbers)
	p.close()
	p.join()
	end_time = time.time()
	total_time_taken = end_time - start_time
	print('time with multi processing',total_time_taken)

def sum_square_no_mp(numbers):
	start_time = time.time()
	result = []
	for i in numbers:
		result.append(sum_square(i))
	#print('wmp:',result)
	end_time = time.time()
	total_time_taken = end_time - start_time
	print('time without multi processing',total_time_taken)

if __name__ == '__main__':
	numbers = range(30000)
	print(numbers)
	sum_square_with_mp(numbers)
	sum_square_no_mp(numbers)
