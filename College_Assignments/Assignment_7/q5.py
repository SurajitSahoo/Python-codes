
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(limit):
    primes = {num for num in range(2, limit + 1) if is_prime(num)}
    return primes


def generate_odds(limit):
    odds = {num for num in range(1, limit + 1) if num % 2 != 0}
    return odds


limit = 50


prime_numbers = generate_primes(limit)
odd_numbers = generate_odds(limit)


union_set = prime_numbers.union(odd_numbers)
intersection_set = prime_numbers.intersection(odd_numbers)
difference_set = prime_numbers.difference(odd_numbers)
symmetric_difference_set = prime_numbers.symmetric_difference(odd_numbers)


print(f"Prime Numbers: {prime_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print(f"Union (Prime ∪ Odd): {union_set}")
print(f"Intersection (Prime ∩ Odd): {intersection_set}")
print(f"Difference (Prime - Odd): {difference_set}")
print(f"Symmetric Difference (Prime Δ Odd): {symmetric_difference_set}")
