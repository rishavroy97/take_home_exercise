# Take Home Exercise - Macquarie Group

## Task
The objective of this exercise is to write a program that takes a single command line argument, a positive integer greater than 1, and **prints out all the prime numbers between 2 and N inclusive**.

>⚠️The program was tested in `python3.12` but it should be backwards compatible for `python3.6+`.

## Project Structure

```
/take_home_exercise
├── primes/             # Python module for prime number generation
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── main.py             # Main python file
```

## Installation Steps

1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Run Instructions

There are two different algorithms: *basic* and *optimized*
1. To execute the main program with the basic algo:
    ```bash
    python main.py <integer>
    ```

2. To execute the main program with the optimized algo:
    ```bash
    python main.py <integer> --optimized
    ```

> The prime number generation function is timed to check the performance [For significant performance difference, try N >= 100000]


## Basic Algo

This algorithm is based on the following fact:
> For a number `k` to be prime, it *should not* be divisible by any number from 2 to `sqrt(k)`

The outer loop runs for `n` cycles. For each outer loop cycle, the inner loop runs upto `sqrt(k)` times.
```
    T(n) = sqrt(1) + sqrt(2) + sqrt(3) + ... + sqrt(n)
=>  T(n) = O(n ^ (3/2))   
```

Therefore, **time complexity** for this algo is **`O(n ^ (3/2))`**.

Since, there is no extra space used in this algo, the **space complexity** is **`O(1)`**


## Optimized Algo

The optimized algorithm uses the `Sieve of Eratosthenes` approach of finding prime numbers.
> For each prime number `k`, mark all the multiples of `k` as *non-prime* to reduce calculations

Time complexity for this algorithm can be calculated by identifying the pattern in the number of iterations of the inner loop.
```
    T(n) = O(n/2 + n/3 + n/5 + n/7 + ... + all prime numbers upto n)
```

This sum is related to the harmonic series of prime numbers, which grows logarithmically.

Reference to the calculation: [link](https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes)

Therefore, **time complexity** for this algo is **`O(n log(log n))`**.

Since, the primality status of each number from 0 to n is stored, the **space complexity** is **`O(n)`**
