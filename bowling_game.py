"""
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

n - number of rows of bowls

Bowling

How many bowls do we need given the "n"
"""

def sum_bowls_recurs(n):
    if n == 1:
        return 1
    else:
        prev_n = sum_bowls_recurs(n - 1)
        return prev_n + n


def sum_bowls_loop(n):
    sum_b = 0
    for i in range(1, n + 1):
        sum_b += i
    return sum_b


def sum_bowls_seq(n):
    return round((n*(n+1))/2)


n = 10000000
print(f'sum using sum_bowls_loop,    n={n}: {sum_bowls_loop(n)}')
print(f'sum using sum_bowls_seq,     n={n}: {sum_bowls_seq(n)}')
#print(f'sum using sum_bowls_recurs,  n={n}: {sum_bowls_recurs(n)}')