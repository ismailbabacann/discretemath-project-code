import math

def is_prime(num):
    """Check if a number is a prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes_in_range(start, end):
    """Find twin primes in the given range."""
    twin_primes = []
    for n in range((start + 1) // 6, (end - 1) // 6 + 1):
        p = 6 * n - 1
        q = 6 * n + 1
        if p > start and q < end and is_prime(p) and is_prime(q):
            twin_primes.append((p, q, n))
    return twin_primes

# Define the range (2000, 3002)
start_range = 2000
end_range = 3002

# Find twin primes
results = find_twin_primes_in_range(start_range, end_range)

# Print the results in tabular format
print(f"{'Rank':<5} {'p':<5} {'q':<5} {'(p, q)':} {'n':<5}")
print("-" * 40)
for rank, (p, q, n) in enumerate(results, start=61):
    print(f"{rank:<5} {p:<5} {q:<5} ({p}, {q}):<15 {n:<5}")

# Save results to a file for reproducibility
with open("twin_primes_table_2000_3002.txt", "w") as file:
    file.write(f"{'Rank':<5} {'p':<5} {'q':<5} {'(p, q)':<15} {'n':<5}\n")
    file.write("-" * 40 + "\n")
    for rank, (p, q, n) in enumerate(results, start=61):
        file.write(f"{rank:<5} {p:<5} {q:<5} ({p}, {q}):<15 {n:<5}\n")
