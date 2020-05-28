import itertools

def primes_my():
    n = 1
    while True:
        n +=1
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            yield n


def primes_correct():
    i = 2
    while True:
        is_prime = True
        divisor = 2
        while divisor ** 2 <= i:
            if i % divisor == 0:
                is_prime = False # non-trivial divisor
                break

            divisor += 1

        if is_prime:
            yield i

        i += 1

def primes_wilson():
    c, f = 2, 1
    while True:
        if not (f + 1) % c:
            yield c
        f, c = f * c, c + 1


print(list(itertools.takewhile(lambda x : x <= 1000, primes_wilson())))
