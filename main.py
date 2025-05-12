import argparse
from typing import List
from primes import validate_input, get_algorithm
import time

def list_primes(N: int, optimized: bool = False) -> List[int]:
    """
    List all prime numbers up to N
    """
    algo_type = 'optimized' if optimized else 'basic'
    algorithm = get_algorithm(algo_type)
    return algorithm.list_primes(N)
    
def main():
    parser = argparse.ArgumentParser(description="List prime numbers up to N")
    parser.add_argument("N", type=int, help="Positive integer N - greater than 1")
    parser.add_argument("--optimized", help="Use optimized algorithm for prime generation", default=False, action="store_true")
    args = parser.parse_args()
    
    if not validate_input(args.N):
        raise ValueError("N must be a positive integer greater than 1")
    
    start_time = time.time()
    primes = list_primes(args.N, args.optimized)
    end_time = time.time()
    print("\n".join(str(p) for p in primes))
    
    print(f"Execution time: {(end_time - start_time) * 1000:.3f} milliseconds")

if __name__ == "__main__":
    main()