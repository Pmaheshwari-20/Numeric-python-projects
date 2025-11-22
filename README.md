## Programme 1: 
 A function named euler_phi(n) that computes Euler's totient function φ(n): the number of integers from 1 up to n that are coprime with n (i.e., integers k with gcd(k, n) == 1).

Notes and Working of euler_phi(n):
- The euler_phi(n) function calculates the Euler Totient of the input integer n. The implementation follows a direct counting approach: it iterates through all integers k from 1 up to n and checks if
  gcd(k, n) = 1.
  
- For n ≥ 2, φ(n) is the count of integers k in [1, n] such that gcd(k, n) = 1.

-  Input must be an integer n ≥ 1. 
- φ(1) = 1 is handled explicitly.
- For prime n, φ(n) = n − 1.
- For prime powers p^k, φ(p^k) = p^k − p^(k−1).

## Programme 2:
Write a function called mobius(n) that calculates mobius function. The function is defined as:

a)	µ(n)=1 if n is a square free positive integer with an even number of prime factors.

b)	µ(n)= -1 if n is square free positive integer with an off number of prime factors.

c)	µ(n)=0 if n has a squared factors. 

Working of Mobius Function:
- If n == 1, return 1 (by definition).
- Set count = 0 (this will count distinct prime factors).
  Handle prime 2:
- If 2 divides n, count how many times. If it divides 2 or more times (exponent ≥ 2), return 0 immediately.
- If it divides exactly once, increment count by 1 and divide n by 2.
-Check odd primes p = 3, 5, 7, ... while p*p <= n:
  If p divides n, count how many times it divides.
  If exponent ≥ 2, return 0 immediately.
  If exponent == 1, increment count and divide n by p.
- Continue with the next odd p (you can stop earlier if n becomes 1 or p*p > n).
- After the loop, if n > 1 then the remaining n is a prime factor (count += 1).
- Return 1 if count is even, otherwise return −1.

## Pragramme 3:
Write a function called divisor_sum(n) which calculates all divisors of a number (including 1 and the number itself). This is often denoted as σ(n).

Working and Algorithm :
- This program computes the sum of all positive divisors of a given positive integer n.  
Example: for n = 12, divisors are 1, 2, 3, 4, 6, 12 and the sum is 28.

- The original input program did a simple loop from 1..n and summed divisors, and printed timing and memory information.
1. If n == 1 return 1.
2. Compute r = floor(sqrt(n)).
3. For i from 1 to r:
   - If i divides n, add i and n//i to the sum.
   - If i * i == n, add i only once (avoid double count).
4. Return accumulated sum.

## Programme 4:
Write a function called prime_pi(n) which approximates the prime counting function π(n). this function returns the number of prime numbers equal to or less than n.

Working and Algorithm:
 - For each integer i from 2 to n, test if i is prime by checking divisibility by integers 2..sqrt(i).
1. For i from 2 to n:
   - If i == 2: prime.
   - Else if i % 2 == 0: not prime.
   - Else:
     - For d from 3 to floor(sqrt(i)) step 2:
         - If i % d == 0, not prime.
     - If no divisor found, i is prime.
2. Count primes found.

## Programme 5:
Write a function called legendre_symbol(a, p) that calculates the Legendre symbol (a/p), which is a useful function in quadratic reciprocity. It is defined for an odd prime p and an integer a not divisible by p as: 
(a/p) = 1 if a is a quadratic residue modulo p (i.e., there exists an integer x such that x²= a (mod p)). 
(a/p) = -1 if a is a quadratic non-residue modulo p. 
You can calculate it using Euler's criterion: (a/p)= a^((p-1)/2) mod p.

Working and Algorithm:
- This program computes the Legendre symbol (a/p) for an integer a and an odd prime p. The Legendre symbol is a classical number‑theory function that indicates whether a is a quadratic residue modulo p.

- (a/p) = 1  if there exists x with x^2 ≡ a (mod p) and a ≠ 0 (mod p)
- (a/p) = −1 if no such x exists
- (a/p) = 0  if a ≡ 0 (mod p)
  
 1. Validate inputs:
   - Ensure p is an odd prime (if not, abort).
   - Optionally reduce a modulo p : a_mod = a % p.
 2. If a_mod == 0 return 0.
 3. Compute power = (p − 1) // 2.
 4. Compute value = modular_exponentiation(a_mod, power, p).
   - Use fast binary exponentiation or language built-in pow(a_mod, power, p).
 5. Interpret value:
   - if value == 1 return 1
   - if value == p − 1 return −1
   - else return 0 (should only happen when value == 0)


# Programme 6:
Write a function factorial(n) that calculates the factorial of a non-negative integer n (n!).

Working and Algorithm:
- Iterative multiplication from 2 up to n (inclusive). This is simple, efficient in practice for moderate n, and avoids recursion depth limits.
- n! = 1 × 2 × 3 × ... × n
with the convention 0! = 1.

- Input: non-negative integer n
- Output: integer n!

# Programme 7:
Write a function is_palindrome(n) that checks if a number reads the same forwards and backwards.

Working and Algorithm:
- The original script reads an integer n , reverses its decimal representation and reports whether the reversed string equals the original string. It also prints execution time and an approximate memory usage.
- - Negative numbers are not palindromes (the `-` sign breaks symmetry).
- Leading zeros are not considered (so numbers that end with `0` are not palindromes unless the number is `0`).
- Method used : String method 
       Convert n to string s.
       If s == s[::-1] return True else False.

# Programme 8:
Write a function mean_of_digits(n) that returns the average of all digits in a number. 

Working and Algorithm:
This program computes the arithmetic mean (average) of the decimal digits of an integer `n`.
- Reads an integer `n` from input.
- Converts `n` to string and sums its digits to compute the mean and returns 'mean'.
- Measures execution time using `time.perf_counter()`.
- Attempts to report memory usage using `sys.getsizeof` on the integer and the function result (this is misleading and also causes the function to run twice).


 # Programme 9:
 Write a function digital_root(n) that repeatedly sums the digits of a number until a single digit is 
obtained. 

Working and Algorithm:
- The digital root of a non‑negative integer is the single digit obtained by repeatedly summing its decimal digits until a single digit remains. Commonly used in numerology, checksum checks, and some arithmetic tricks, the digital root can be computed efficiently without iterating over digits.

- The code reads an integer `n`.
- Defines a compact function using the 1 + (n−1) % 9 trick, which is correct for non‑negative integers.
- Measured execution time using `time.perf_counter()`.
- Attempts to measure memory by calling `sys.getsizeof` on `n` and on `digital_root(n)`; that yields the sizes of those small integer objects.


# Programme 10:
Write a function is_abundant(n) that returns True if the sum of proper divisors of n is greater than n. 

Working and Algorithm:

This program determines whether a given positive integer `n` is abundant.
- A number is abundant if the sum of its proper divisors (divisors less than `n`) is greater than `n`.
- Example: 12 has proper divisors 1,2,3,4,6 — sum = 16 > 12 → 12 is abundant.
- The code iterates through range 1 to n and increments count c with i when i%n results in value 0.
- The code returns boolean value True when c>n and returns False when otherwise.
- also measures elapsed time with 'time.perf_counter' and memory utlised with 'sys.getsizeof'.

# Programme 11:
Write a function is_deficient(n) that returns True if the sum of proper divisors of n is less than n.

Working and Algorithm:

- A number n is deficient if the sum of its proper divisors (all positive divisors excluding n itself) is strictly less than n.
  -Example: 8 has proper divisors 1, 2, 4 (sum = 7) → 7 < 8, so 8 is deficient.
    -12 has proper divisors 1,2,3,4,6 (sum = 16) → 16 ≥ 12, so 12 is not deficient.

1. Handles small inputs:
   - If n <= 1: proper divisors sum = 0 (so n=1 is deficient).
2. Computes sum of proper divisors efficiently by iterating i from 1 to sqrt(n):
   - For each divisor i that divides n:
     - Add i
     - If i != 1 and i != n//i (and the paired divisor != n), add paired divisor n//i
   - Exclude n from the sum (proper divisors only).
3. Compares the sum with n.


# Programme 12:
Write a function for harshad number is_harshad(n) that checks if a number is divisible by the sum of its digits.

Working and Algorithm:

- A Harshad (or Niven) number is an integer that is divisible by the sum of its decimal digits.
  - Example: 18 → digits 1 + 8 = 9 and 18 % 9 == 0, so 18 is a Harshad number.

1. Computes the sum of decimal digits of |n|.
2. If digit sum is 0 (only possible when n == 0)
   - Define is_harshad(0) = False (or True depending on convention).
3. Returns (n % digit_sum == 0).


# Programme 13:
Write a function is_automorphic(n) that checks if a number's square ends with the number itself.

Working and Algorithm:

- A number n is automorphic if n^2 ends with the decimal representation of n.
  - Example: 5 → 5^2 = 25 ends with "5" → automorphic.

1. Computes m = number of digits of n (or modulus = 10^m).
2. Computes n_squared = n * n.
3. Checks if n_squared % (10^m) == n.


# Programme 14:
Write a function is_pronic(n) that checks if a number is the product of two consecutive integers.

Working and Algorithm:
- A pronic number (also called oblong or heteromecic) is a number that is the product of two consecutive integers:
  n is pronic if there exists an integer k >= 0 such that n = k * (k + 1).
  - Examples:
    - 6 = 2 * 3 → pronic
    - 20 = 4 * 5 → pronic

-  Solves i*(i+1) = n for integer i >= 0.
- When the quadratic equation i^2 + i gives n then prints true.

# Programme 15:
Write a function prime_factors(n) that returns the list of prime factors of a number.

Working and Algorithm:
- prime_factors(n) returns the prime factors of n as a list.
  - our variant: full factorization with multiplicity, e.g. prime_factors(360) -> [2, 2, 2, 3, 3, 5].

1. Validates input: if n == 0: raise ValueError
2. Removes factors of 2 in a loop, appending 2 each time.
3. For odd candidate p starting at 3 and increasing by 2 while p*p <= n:
   - While n % i == 0:
     - append i; n //= i.
4. If remaining n > 1 after the loop, it is prime — append n.
5. Returns the factors list.





