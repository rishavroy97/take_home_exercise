from primes.util import validate_input
from primes.algos.basic_algo import BasicAlgorithm
from primes.algos.optimized_algo import OptimizedAlgorithm
from primes.algos.algo import PrimeAlgorithm

def get_algorithm(option: str) -> PrimeAlgorithm:
    """
    Get the appropriate prime number algorithm based on the user's choice.
    Args:
        option (str): The algorithm option chosen by the user ('basic' or 'optimized').
    Returns:
        PrimeAlgorithm: An instance of the selected prime number algorithm.
    """
    algos = {
        'basic': BasicAlgorithm,
        'optimized': OptimizedAlgorithm
    }
    
    if option not in algos:
        raise ValueError(f"Invalid algorithm option: {option}. Choose 'basic' or 'optimized'")
    
    return algos[option]()