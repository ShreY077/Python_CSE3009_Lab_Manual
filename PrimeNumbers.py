def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Check divisibility by odd numbers up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

# Test the function
n = int(input("Enter the value of n: "))
print("First", n, "prime numbers are:")
print_first_n_primes(n)
