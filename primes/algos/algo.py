from abc import ABC, abstractmethod
from typing import List

class PrimeAlgorithm(ABC):
    """
    Abstract base class for prime number algorithms.
    """

    @abstractmethod
    def list_primes(self, n: int) -> List[int]:
        """
        List all prime numbers up to n.
        Args:
            n (int): The upper limit for prime number generation
        Returns:
            List[int]: A list of prime numbers up to n
        """
        pass