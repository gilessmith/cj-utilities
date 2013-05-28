from decimal import *

# this is for super precise calculations - calculations accurate to 300 dp's
getcontext().prec = 300

def solve_quadratic(a, b, c):
    
    discriminant = Decimal(b) ** Decimal(2) - Decimal(4*a*c)
    if discriminant < 0:
        raise Exception('No real roots')
    else:
        discriminant = Decimal(discriminant) **Decimal(0.5)

    small_result = (Decimal(-1) * b - discriminant) / (Decimal(2 * a))
    large_result = (Decimal(-1) * b + discriminant) / (Decimal(2 * a))

    return small_result, large_result
    

def test():
    small_root, large_large = solve_quadratic(3, 7, -6)

    assert small_root == Decimal(-3)
    assert large_large == Decimal(2) / 3

    print "Tests Passed"
    

if __name__ == '__main__':
    test()
