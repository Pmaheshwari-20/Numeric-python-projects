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

# Programme 16:
Write a function count_distinct_prime_factors(n) that returns how many unique prime factors a number has.

Working and Algorithm:
-A small utility that counts how many distinct prime factors a given integer has.

1. Normalizes input:
   - Convert to integer (int(n))

2. Handle factor 2:
   - If n is divisible by 2, increments the distinct-prime counter by 1.
   - Repeatedly divides n by 2 until it's no longer divisible.

3. Trial division by odd numbers:
   - For every odd integer f starting at 3 and increasing by 2 while f * f <= n:
     - If f divides n, you've found a new distinct prime factor:
       - Increment the counter by 1.
       - Divide n repeatedly by f until it's no longer divisible.
   - This ensures each prime factor is counted only once.

4. If after the loop n > 1:
   - The remaining n is a prime greater than sqrt(original n); count it once.

# Programme 17:
Write a function is_prime_power(n) that checks if a number can be expressed as pk where p is prime and k ≥ 1.

Working and Algorithm:
- Given an integer n, decides if there exist a prime p and an integer k >= 1
such that n = p^k.

- Normalizes and rejects:
  - Convert to int; if n <= 1 or n < 0, return False (1 is not p^k with k >= 1).

- Factorization by trial division:
  - Use the standard trial-division approach: iterates p with p raise to the power k in range 2 to n+1.
  - Returns truw if power == n. Returns false otherwise.

- Decision:
  - If more than one distinct prime factor is found at any point, n is not a prime power.
  - If exactly one distinct prime factor remains (possibly after removing all
    powers), n is a prime power.

 
 # Programme 18:
 Write a function is_mersenne_prime(p) that checks if 2p - 1 is a prime number (given that p is prime).

 Working and Algorithm:
 
 Given an integer p, decide whether M_p = 2^p - 1 is prime. Note: the Lucas–Lehmer test applies only when p itself is prime.

 1. Normalizes input:
   - Converts to integer: p = int(p).
   - If p < 2, returns False (exponent too small).

 2. Verifies if  p is prime:
   - Use a fast primality test for p.
   - If p is composite, M_p cannot be prime, so return False early.

 3. Lucas–Lehmer test (deterministic for prime exponent p):
   - If p == 2, M_p = 3 which is prime (return True).
   - Let n = 2^p - 1.
   - iterates j in range 2 to sqrt n +1. if n mod j results zero; returns false.
   - Else returns true.
   - doesnt run for negative input,


# Programme 19:
Write a function twin_primes(limit) that generates all twin prime pairs up to a given limit.

Working and Algorithm:
- Given an integer limit, produces all twin-prime pairs (p, p+2) such that both p and p+2 are prime and p+2 <= limit.

 1. Normalizes input:
   - Converts the input to int (the provided script uses x.isdigit() then int(x)).
   - If the integer is <= 2, there are no twin primes -> return [False].

 2. For each integer i from 2 to limit-2:
   - Uses trial-division primality test on i.
   - Uses trial-division primality test on i+2.
   - If both are prime, records the pair (i, i+2).
   - For every twin-prime pair (p, p+2) with p+2 <= limit, the loop will reach i == p and record it.
   - The trial-division primality test is deterministic and correct for integer inputs.


# Programme 20:
Write a function Number of Divisors
(d(n)) count_divisors(n) that returns how many positive divisors a number has.

Working and Algorithm:
 -Given a positive integer n, compute the number of positive divisors of n.
 - Example session

     Input: 28

     Output:

     Number of divisors: 6
   
  - Iterates i from 1 to n inclusive.
  - If n % i == 0, increments count.
  - Returns count.
  - checks every possible divisor.

# Programme 21:
Write a function aliquot_sum(n) that returns the sum of all proper divisors of n (divisors less than n).

Working and Algorithm:
- Given a (positive) integer n, computes the aliquot sum:

  s(n) = sum_{d | n, 1 <= d < n} d

i.e., the sum of all positive proper divisors of n.

-  1. Initializes sum = 0.
  2. iterates  i from 1 to n-1:
       checks if  n % i == 0 and then increments the variable sum by i
  3. Returns value of sum to the function.


# Programme 22:
Write a function are_amicable(a, b) that checks if two numbers are amicable (sum of proper divisors of a equals b and vice versa).

Working and Algorithm:
- Provides proper_divisor_sum(n): sum of proper divisors of n (positive integers < n that divide n)
- Checks if are_amicable(a, b): returns True if a and b form an amicable pair, otherwise False
-Examples:

  >>> are_amicable(220, 284)

  True

1. Normalizes and validates inputs:
   - Converts the  inputs to integers (int(a), int(b)). If conversion fails, raises an error.
   - If either integer <= 0, return False (amicable numbers are positive).
   - If a == b, return False (perfect numbers are not considered amicable pairs here).

2. Computes the sum of proper divisors:
   - Computes s(a) = sum of proper divisors of a.
   - If s(a) != b, returns False immediately (early exit).
   - Otherwise computes s(b) and checks if s(b) == a.
  

# Programme 23:
Write a function multiplicative_persistence(n) that counts how many steps until a number's digits multiply to a single digit.

Working and Algorithm:
- The multiplicative persistence of a non-negative integer n is the number of times you must multiply the digits of n together until you reach a single-digit number.
  Example: 39 -> 3*9 = 27 (1 step) -> 2*7 = 14 (2 steps) -> 1*4 = 4 (3 steps) so persistence(39) = 3.

 1. Reads input n = int(input(...)).
 2. Initialize a counter c = 0.
 3. While n >= 10 (i.e., n has at least two digits):
   a. Convert n to its decimal string representation.
   b. Computes the product p of all digits: iterates each character d in str(n) and multiplies p *= int(d).
   c. Sets n = p and increments c.
 4. Returns c (the persistence count)
- Each loop computes the exact product of digits with integer arithmetic; repeated application follows the definition.
- The loop terminates because eventually the process reaches a single-digit number (0..9), at which point n < 10 and the loop stops.


# Programme 24:
Write a function is_highly_composite(n) that checks if a number has more divisors than any smaller number.

Working and Algorithm:
- the programme checks whether a given positive integer n is a highly composite number (HCN).
- According to the usual definition: n is highly composite if the number of positive divisors of n is strictly greater than the number of divisors of any smaller positive integer.

   1. For each integer i from 1 to n-1:
       - Computes d(i) by testing all potential divisors j from 1 to i:

         computes d(i) = sum(1 for j in 1..i if i % j == 0)
       - Tracks max_divisors = max(max_divisors, d(i))
  2. Computes d(n) similarly by testing divisors 1..n.
  3. Returns d(n) > max_divisors.


# Programme 25:
Write a function for Modular Exponentiation mod_exp(base, exponent, modulus) that efficiently calculates (baseexponent) % modulus.

Working and Algorithm:
 The function mod_exp(n1, n2, n3) implements the standard iterative binary exponentiation:
  - It first reduces the base modulo n3 (n1 = n1 % n3).
  - Repeatedly squares the base and, when the current exponent bit is 1, multiplies the result by the base (mod n3).
  -   Example session
     Enter the base: 4

      enter the exponent: 13
 
      enter the modulus: 497

      result:  445

  - The algorithm maintains the invariant:

    base_original^exponent = result * base^(e) (mod modulus)

    where `e` is the remaining exponent. Each step either consumes a 1-bit of e by multiplying result by base, or squares base and halves e. This correctly computes base_original^exponent mod modulus.


      



