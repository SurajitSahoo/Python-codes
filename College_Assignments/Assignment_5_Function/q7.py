class GCDCounter:
    def __init__(self):
        self.call_count = 0
    
    def gcd(self, a, b):
        self.call_count += 1
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

# Example usage:
counter = GCDCounter()
num1 = 48
num2 = 18
result = counter.gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")  # Output: GCD of 48 and 18 is 6
print(f"Number of recursive calls: {counter.call_count}")  # Output: Number of recursive calls: 3
