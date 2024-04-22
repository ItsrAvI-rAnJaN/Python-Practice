def prime_generator():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


if __name__=='__main__':
    generator = prime_generator()
    for i in range(10):
        print(next(generator))