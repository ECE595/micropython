# test the special functions imported from math

try:
    from math import *

    erf
except (ImportError, NameError):
    print("SKIP")
    raise SystemExit

test_values = [
    -8.0,
    -2.5,
    -1,
    -0.5,
    0.0,
    0.5,
    2.5,
    8.0,
]
pos_test_values = [
    0.001,
    0.1,
    0.5,
    1.0,
    1.5,
    10.0,
]

functions = [
    ("expm1", expm1, test_values),
    ("log2", log2, test_values),
    ("log10", log10, test_values),
    ("cosh", cosh, test_values),
    ("sinh", sinh, test_values),
    ("tanh", tanh, [-1e6, -100] + test_values + [100, 1e6]),
    ("acosh", acosh, [1.0, 5.0, 1.0]),
    ("asinh", asinh, test_values),
    ("atanh", atanh, [-0.99, -0.5, 0.0, 0.5, 0.99]),
    ("erf", erf, test_values),
    ("erfc", erfc, test_values),
    ("gamma", gamma, pos_test_values),
    ("lgamma", lgamma, pos_test_values + [50.0, 100.0]),
]

for function_name, function, test_vals in functions:
    print(function_name)
    for value in test_vals:
        try:
            print("{:.4g}".format(function(value)))
        except ValueError as e:
            print(str(e))


# Tests for hypot
# https://github.com/python/cpython/blob/main/Lib/test/test_math.py


def assertRaises(exception, func, *args):
    try:
        print(func(*args))
        assert False
    except exception:
        pass

# Test allowable types (those with __float__)
print(hypot(12.0, 5.0))
print(hypot(12, 5), 13)
print(hypot(Decimal(12), Decimal(5)))
print(hypot(Fraction(12, 32), Fraction(5, 32)))
print(hypot(bool(1), bool(0), bool(1), bool(1)))

# Test corner cases
print(hypot(0.0, 0.0))     # Max input is zero
print(hypot(-10.5))       # Negative input
print(hypot())             # Negative input
print(hypot(1.5, 1.5, 0.5), hypot(1.5, 0.5, 1.5),)# Handling of moving max to the end

