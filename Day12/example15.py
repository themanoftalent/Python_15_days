import itertools

from math import sqrt

from concurrent.futures import ProcessPoolExecutor

from time import time

def is_prime(n):
    if n < 2:
        return False
    for number in range(2, int(sqrt(n)) + 1):
        if n % number == 0:
            return False
    return True

def main():
    numbers = [number for number in range(1000000, 1001000)]
    start = time()
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(numbers, executor.map(is_prime, numbers)):
            print('%d is prime: %s' % (number, prime))
    print('Time: %.3f seconds' % (time() - start))

if __name__ == '__main__':
    main()
