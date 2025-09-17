# Problem 5

$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from $1$ to $20$?

## Solution to the test case

The prime numbers between $1$ and $10$ are: $2$, $3$, $5$ and $7$, so the least common multiple must have these numbers ($2\times3\times5\times7$). If the rest of the numbers can be obtained with the primes, they are already taken into account. So, for example, $6$ is taken into account as $2\times3=6$ and $4$, $8$ and $9$ are not.

To get $4$ we have to add a second $2$, to get $8$ a third $2$, and a second $3$ to get $9$. So the least common multiple for all numbers between 1 and 10 is $2\times2\times2\times3\times3\times5\times7=2520$.

## Solution to the problem

We have to get the least common multiple by the same analysis as explained above.

- First get the prime numbers ($2$, $3$, $5$, $7$, $11$, $13$, $17$, $19$).
- To get $4$ add a second $2$.
- To get $8$ add a third $2$.
- To get $9$ add a second $3$.
- To get $16$ add a fourth $2$.
- Result: $2\times2\times2\times2\times3\times3\times5\times7\times11\times13\times17\times19=232792560$

## Computational solution

Applies the same logic that explained above.
