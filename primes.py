def primes(N):
    if N >= 1 and N <= 100000:
        primes = 0

        for i in range(2, N):
            prime = True

            for k in range(2, i):
                if i % k == 0:
                    prime = False
                    
                    break
            
            if prime:
                primes += 1
    else:
        exit(0)

    return primes

if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15