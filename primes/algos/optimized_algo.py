from primes.algos.algo import PrimeAlgorithm

class OptimizedAlgorithm(PrimeAlgorithm):
    def list_primes(self, n: int) -> list:
        """
        List all prime numbers using Sieve of Eratosthenes algorithm.
        Args:
            n (int): The upper limit for prime number generation
        Returns:
            List[int]: A list of prime numbers up to n
        """
        
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as non-prime
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        return [i for i in range(n + 1) if is_prime[i]]