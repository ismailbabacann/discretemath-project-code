# Finding prime numbers with Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

# Function to count twin prime numbers
def count_twin_primes(limit):
    primes = sieve_of_eratosthenes(limit)
    twin_prime_count = 0
    # Count twin prime numbers
    for i in range(1, len(primes)):
        if primes[i] - primes[i-1] == 2:
            twin_prime_count += 1
    return twin_prime_count

# Given N values
N_values = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10,
            10**11, 10**12, 10**13, 10**14, 10**15, 10**16, 10**17, 10**18]

# Calculate and print results
print(f"{'N':<15}{'Twin Primes Count':<20}{'Prime Count':<15}{'% Twin Primes'}")
for N in N_values:
    twin_prime_count = count_twin_primes(N)
    prime_count = len(sieve_of_eratosthenes(N))  # Count prime numbers between 1 and N
    twin_prime_percentage = (twin_prime_count / prime_count) * 100 if prime_count > 0 else 0
    print(f"{N:<15}{twin_prime_count:<20}{prime_count:<15}{twin_prime_percentage:.2f}")
