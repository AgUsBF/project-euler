# Problem 9

A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which, $a^2 + b^2 = c^2$. For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$. Find the product $abc$.

## Solution

Taking into accout that $a \lt b \lt c$ and $a + b + c = N$ we get:

$$3\ a \lt a + b + c = N$$

So, as all numbers are naturals

$$1 \lt a \lt \frac{N}{3}$$

From the Pythagorean equation, and by replacing the term $c$ we can get:

$$b = \frac{N - 2\ a}{2} \times \frac{N}{N - a}$$

and

$$c = \sqrt{a^2 + b^2}$$

To get the final solution, just iterate the posible values of $a$, calculate $b$ and $c$, check if the values are integers, and when they do (there is only one possible combination), return the product $abc$.
