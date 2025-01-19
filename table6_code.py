import math
import time

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to count twin primes up to a limit
def count_twin_primes(limit):
    twin_primes_count = 0
    for n in range(1, limit // 6 + 1):
        p = 6 * n - 1
        q = 6 * n + 1
        if p < limit and q < limit and is_prime(p) and is_prime(q):
            twin_primes_count += 1
    return twin_primes_count

# Limits to test
limits = [1000, 10000, 100000, 1000000]

# List to store results
results = []

# Measure execution time for each limit
for limit in limits:
    start_time = time.time()
    twin_primes_found = count_twin_primes(limit)
    execution_time = time.time() - start_time
    results.append((limit, twin_primes_found, round(execution_time, 2)))

# Print the table in the requested format
print(f"Limit              Twin Primes Found    Execution Time (seconds)")
for limit, twin_primes, exec_time in results:
    print(f"{limit:>10,} {twin_primes:>15,} {exec_time:>20.2f}")

# Save results to a file
with open("twin_primes_execution_results.txt", "w") as file:
    file.write("Limit              Twin Primes Found    Execution Time (seconds)\n")
    for limit, twin_primes, exec_time in results:
        file.write(f"{limit:>10,} {twin_primes:>15,} {exec_time:>20.2f}\n")
