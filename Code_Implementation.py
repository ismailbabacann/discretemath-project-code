# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find all twin primes up to a given limit
def find_twin_primes(limit):
    twin_primes = []
    previous_prime = 2
    for num in range(3, limit + 1):
        if is_prime(num):
            if num - previous_prime == 2:
                twin_primes.append((previous_prime, num))
            previous_prime = num
    return twin_primes

# Finding twin primes up to a specified limit
limit = 10000  # You can adjust this value for larger experiments
twin_primes = find_twin_primes(limit)

# Output the results
print(f"Twin primes up to {limit}:")
print(twin_primes)
