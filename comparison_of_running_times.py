
"""
1-1 Comparison of Running Times (CLRS)

For each function f(n) and time t in the following table, determine the
largest size n of a problem that can be solved in time t, assuming that
the algorithm to solve the problem takes f(n) microseconds.
"""

import math

# ================================
# Time Limits (in microseconds)
# ================================
TIMES = {
    "1 second": 1_000_000,
    "1 minute": 60 * 1_000_000,
    "1 hour": 3600 * 1_000_000,
    "1 day": 86400 * 1_000_000,
    "1 month": 30 * 86400 * 1_000_000,
    "1 year": 365 * 86400 * 1_000_000,
    "1 century": 100 * 365 * 86400 * 1_000_000
}


# ================================
# Solvers for each complexity
# ================================
def solve_logn(t):
    return f"2^{t}"   # ✅ symbolic (prevents overflow)

def solve_sqrtn(t):
    return int(t ** 2)

def solve_n(t):
    return int(t)

def solve_nlogn(t):
    lo, hi = 1, t
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * math.log2(mid) <= t:
            lo = mid
        else:
            hi = mid - 1
    return lo

def solve_n2(t):
    return int(math.sqrt(t))

def solve_n3(t):
    return int(t ** (1 / 3))

def solve_2n(t):
    return int(math.log2(t))

def solve_fact(t):
    n = 1
    fact = 1
    while fact <= t:
        n += 1
        fact *= n
    return n - 1


# ================================
# Complexity Map
# ================================
FUNCTIONS = {
    "log n": solve_logn,
    "√n": solve_sqrtn,
    "n": solve_n,
    "n log n": solve_nlogn,
    "n²": solve_n2,
    "n³": solve_n3,
    "2ⁿ": solve_2n,
    "n!": solve_fact
}


# ================================
# Print Results Table
# ================================
print("\n MAXIMUM n FOR EACH TIME LIMIT\n")

header = ["Function"] + list(TIMES.keys())
print("{:<12}".format(header[0]), end="")
for h in header[1:]:
    print("{:>16}".format(h), end="")
print("\n" + "-" * 125)

for fname, solver in FUNCTIONS.items():
    print("{:<12}".format(fname), end="")
    for t in TIMES.values():
        val = solver(t)
        print("{:>16}".format(str(val)), end="")
    print()
