import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Generate twin primes and their properties
def generate_twin_primes():
    twin_primes = []
    n_values = []

    # Manually add the first twin prime pair (3, 5) with n = "/"
    twin_primes.append((3, 5))
    n_values.append("/")  # Special case for rank = 0

    # Start generating twin primes using 6n - 1 and 6n + 1
    n = 1
    while len(twin_primes) < 35:  # Stop when we reach rank 34
        p = 6 * n - 1
        q = 6 * n + 1
        if is_prime(p) and is_prime(q):
            twin_primes.append((p, q))
            n_values.append(n)
        n += 1

    return twin_primes, n_values

# Generate the twin primes and corresponding n values
twin_primes, n_values = generate_twin_primes()

# Prepare the data for the table
results = []
for rank, ((p, q), n) in enumerate(zip(twin_primes, n_values), start=0):
    results.append((rank, p, q, f"({p}, {q})", n))

# Print the table
header = f"{'Rank':<5} {'p':<5} {'q':<5} {'(p, q) = (6n−1, 6n+1)':<30} {'n':<5}"
print(header)
print("-" * len(header))
for rank, p, q, pair, n in results:
    print(f"{rank:<5} {p:<5} {q:<5} {pair:<30} {n:<5}")

# Optionally save the results to a text file
with open("twin_primes_table.txt", "w") as file:
    file.write(header + "\n")
    file.write("-" * len(header) + "\n")
    for rank, p, q, pair, n in results:
        file.write(f"{rank:<5} {p:<5} {q:<5} {pair:<30} {n:<5}\n")
