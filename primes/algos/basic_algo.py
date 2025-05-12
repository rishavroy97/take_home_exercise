from primes.algos.algo import PrimeAlgorithm


class BasicAlgorithm(PrimeAlgorithm):
    def list_primes(self, n: int) -> list:
        """
        List all prime numbers up to n using the basic algorithm.
        Args:
            n (int): The upper limit for prime number generation
        Returns:
            List[int]: A list of prime numbers up to n
        """
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            # Check if num is prime by testing divisibility from 2 to sqrt(num)
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes